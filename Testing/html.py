from html2image import Html2Image
from html_test_code import x
import discord
def html_compiler( html, userName="default"):
    htmlObj = Html2Image(custom_flags=['--default-background-color=0', '--virtual-time-budget=20000'])

    try:
        htmlOutput = htmlObj.screenshot(html_str=html, save_as=f"{userName}.png", size=(1920, 1080))
        # file = discord.File(htmlOutput[0])
        # return file
        print(htmlOutput[0])
    except Exception as e:
        print(e)

html_compiler(x)
