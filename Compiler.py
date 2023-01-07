# all of the compiler functions should execute the output and either pass the output to the output function or pass the error to the error function

from html2image import Html2Image # For html function
from js2py import eval_js # for javascript
import discord # for creating a discord file then returning it to the bot
import re # for text processing
import subprocess # for python compiler

class Compiler():

    def __init__(self):
        pass

    def language_selector(self, code = None, language = None, userName = "default"):
        # list of the keywords that are similar to the function name (in case the user misspells anything)
        keywords_list = {"python": ["python", "py", "pyhon", "pyton", "pyon"],
                         "kotlin": [],
                         "javascript": ["javascript", "scrip", "javascript", "js"],
                         "html": ["html", "ht", "thmt", "htm", "tmhl", "lmth"],
                         "php": [],
                         "cpp": ["cpp", "cp", "c++", "cplusplus", "c+-","c==", "c"],
                         "java": []
                         }

        if code is None:
            return self.error_handling("empty")

        if language in keywords_list["python"]:
            return self.python_compiler(code)

        if language in keywords_list["html"]:
            return self.html_compiler(code, userName)

        if language in keywords_list["javascript"]:
            return self.javascript_compiler(code)

        if language in keywords_list["cpp"]:
            return self.cpp_compiler(code)


    def python_compiler(self, code):
        output = subprocess.run(['python', '-c', code], capture_output=True, text=True)

        if output.returncode == 0:
            output = output.stdout
        else:
            output = output.stderr

        return self.output_formatting(output)


    def error_handling(self, error):
        return error

    def kotlin_compiler(self):
        pass


    def javascript_compiler(self, code):
        output = eval_js(code)
        print(output)
        # try:
        #
        #     return self.output_formatting(output)
        # except Exception as e:
        #     return self.error_handling(f"""{e}""")

    def html_compiler(self, html, userName):
        htmlObj = Html2Image(custom_flags=['--default-background-color=0', '--virtual-time-budget=10000'])
        try:
            htmlOutput = htmlObj.screenshot(html_str=html, save_as=f"{userName}.png", size=(1920, 1080))
            output = discord.File(htmlOutput[0])
            return output
        except Exception as e:
            return self.error_handling(f"{e}")

    def php_compiler(self):
        pass



    def cpp_compiler(self, code):
        code = self.replace_word(code, "using", "\nusing")
        code = code.replace("\n", "\\n")
        code = self.replace_word(code, "int", "\nint")
        code = self.replace_word(code, "void", "\nvoid")
        code = self.replace_word(code, "float", "\nfloat")
        code = self.replace_word(code, "double", "\ndouble")
        code = self.replace_word(code, "bool", "\nbool")

        # creates the environment for code execution
        process = subprocess.Popen(['g++', '-x', 'c++', '-o', 'code', '-'], stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

        # runs the program to check for any errors that is not inside the code
        output, error = process.communicate(input=code.encode())
        if process.returncode != 0:
            return self.output_formatting(error.decode())
        else:
            # runs the code if there is no errors
            try:
                process = subprocess.Popen(['code'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                           stdin=subprocess.DEVNULL)
                output, _ = process.communicate()
                return self.output_formatting(output.decode())
            except Exception as e:
                return self.output_formatting(str(e))

    def java_compiler(self):
        pass

    # handles all of the errors by the other functions so the program won't crash
    def output_formatting(self, output):
        if len(output) == 0:
            embedVar = discord.Embed(title="OUTPUT", description=f"There is no output", color=0x00ff00)
            return embedVar

        if len(output) > 1999:
            return f"```{len( output)}```"
        else:
            embedVar = discord.Embed(title="OUTPUT", description=f"{output}", color=0x00ff00)

            return embedVar

    def replace_word(self, string, old_word, new_word):
        # Use a regular expression to match the word boundaries
        pattern = r"\b" + old_word + r"\b"
        return re.sub(pattern, new_word, string)



# implements timout for the functions so the program won't crash or stop workin g


# Uses embed to format the output then returns the embed object to be used by the discord bot
# limits the output



# Shows a formatted output of what can be done using the class aka a list of the available compiler functions
def help(self, output):
    pass
