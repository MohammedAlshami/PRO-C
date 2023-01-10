# This file should process the commands, and pass the processed input to the compiler class
# This should have a general help function for all things that can be done with the bot
import os
import uuid

import discord
from discord import app_commands
from discord.ext import commands
from private.bot_tokens import discord_token
from Compiler import Compiler
from OpenAi import write_code
import nest_asyncio

nest_asyncio.apply()
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
comp = Compiler()


@bot.event
async def on_ready():
    print("Bot is Up and ready")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

    # Removing bot is thinking message
    await bot.change_presence(activity=None)


@bot.command(language="python", help="execute python script")
async def run(ctx, *, arg =""):
    # making the bot wait for the output
    await ctx.defer()


    # Parsing the input
    arg = arg.split(' ', 1)
    if len(arg) > 1:
        # deleting the message
        await ctx.message.delete()
        language = arg[0]
        code = arg[1].lstrip(' ')
        code = code.strip("`")
        # Getting the output
        output = None
        try:
            output = comp.language_selector(code, language.lower(), ctx.message.author.name)
        except Exception as e:
            await ctx.send(f"An error has occurred: {e}")

        if type(output) == discord.Embed:
            await ctx.send(embed=output)
        elif type(output) == discord.file.File:
            await ctx.send(file=output)
        else:
            await ctx.send(f"{output}")
    else:
        # create error embed
        embedVar = discord.Embed(title="Command", description=f"```!run has 2 arguments (language, code)```", color=0xFF0000)
        embedVar.set_footer(text="Bot made by Shami#5662", icon_url="https://i.imgur.com/Chntn67.png")
        await ctx.send(embed=embedVar)


@bot.tree.command(name="chatgpt")
@app_commands.describe(prompt="Write something")
async def chatgpt(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer()

    try:
        output = write_code(f"""{prompt}""", "python")
    except Exception as e:
        output = discord.Embed(title="Error", description=f"```We're sorry but the output couldn't be generated. Try again!```", color=0xFF0000)
        output.set_footer(text="Bot made by Shami#5662", icon_url="https://i.imgur.com/Chntn67.png")


    await interaction.followup.send(embed=output)




@bot.tree.command(name="html")
@app_commands.describe(code="put your html source code here")
async def html(interaction: discord.Interaction, code: str):
    # generating a unique id to identify user's images
    file_name = f"{str(uuid.uuid4())}.png"

    # making the bot wait for the output
    await interaction.response.defer()

    # Getting the output as a tuple (file, embed, absolute filepath as a string)
    output = None
    try:
        output = comp.language_selector(code, "html", file_name)
    except Exception as e:
        await interaction.followup.send(f"An error has occurred: {e}")

    # Sending the message to the user
    await interaction.followup.send(file=output[0], embed=output[1])

    # closing the discord file
    output[0].close()

    # deleting the file once the process is done
    os.remove(output[2])


@bot.tree.command(name="help")
async def help(interaction: discord.Interaction):
    # making the bot wait for the output
    await interaction.response.defer()
    await interaction.followup.send(embed=comp.help())



bot.run(discord_token)
