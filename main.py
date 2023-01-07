# This file should process the commands, and pass the processed input to the compiler class
# This should have a general help function for all things that can be done with the bot
import discord
from discord import app_commands
from discord.ext import commands
from private.bot_tokens import discord_token

from Compiler import Compiler

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



@bot.tree.command(name="run")
@app_commands.describe(language = "Choose the programming language", code = "Copy and paste your code in the input box. (Must be less than 6000 characters")
async def run(interaction: discord.Interaction,  language :str, code: str):
    # solving the 3 seconds issue (without it the program crash if it has to wait for a function to finish
    await interaction.response.defer()

    # error handling
    output = ""
    try:
        output = comp.language_selector(code, language.lower(), interaction.user.name)
    except Exception as e:
        await interaction.followup.send(f"An error has occurred: {e}")

    if type(output) is discord.file.File:
        await interaction.followup.send(file=output)
    elif type(output) is discord.Embed:
        await interaction.followup.send(embed=output)
    else:
        await interaction.followup.send(f"{output}")

@bot.tree.command(name="chatgpt")
@app_commands.describe(prompt = "Write something")
async def chatgpt(interaction: discord.Interaction, prompt: str):
    # await interaction.response.defer()

    # output = debug(f"""{prompt}""", "python")
    # await interaction.response.send_message(output)
    pass


bot.run(discord_token)



