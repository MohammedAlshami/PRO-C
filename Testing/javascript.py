from py_mini_racer import MiniRacer
def javascript_compiler( code):
    ctx = MiniRacer()
    output = ""
    try:
        output = ctx.eval(code)
    except Exception as e:
        output = e

    print(output)


code_snippets = """
// program to convert date to number // create date const d1 = new Date(); console.log(d1);  // converting to number const result = d1.getTime(); console.log(result);
"""

javascript_compiler(code_snippets.replace("document.write", "return"))
