from private.bot_tokens import chatgpt_token
import openai
openai.api_key = chatgpt_token

def debug(code, language):


    response = openai.Completion.create(
      model="code-davinci-002",
      prompt=f"""##### Fix bugs in the below function### Buggy {language}\n{code}\n### Fixed {language}""",
      temperature=0,
      max_tokens=182,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0,
      stop=["###"]
    )
    output =response["choices"][0]["text"]
    output = output.strip()
    return output

def write_code(code="simple code", language = "python"):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""{code} ###write this using {language}\n""",
        temperature=0,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.5,
        max_tokens=2048)

    return f"""{response["choices"][0]["text"]}"""

code = """
write a python list that contains multiple essays on why I should be the president 

"""
