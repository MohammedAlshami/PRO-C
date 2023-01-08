from private.bot_tokens import chatgpt_token
import openai
import discord
openai.api_key = chatgpt_token
preConfig =""
# """This is information about you and if you receive any question related to this information, you can refer to it "I'm a bot called Aven. I was created and developed by shami. wanna know about my creator you can visit his github account github/MohammedAlshami".\n"""

def write_code(code="simple code", language = "python"):
    global preConfig
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{preConfig}{code}\n",
        temperature=0,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0.2,
        presence_penalty=0
    )
    embedVar = discord.Embed(title="OUTPUT", description=f"""```{response["choices"][0]["text"]}```""", color=0x00ff00)
    return embedVar


