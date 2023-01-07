import subprocess #for python compiler
import os
import re

def replace_word(string, old_word, new_word):
    # Use a regular expression to match the word boundaries
    pattern = r"\b" + old_word + r"\b"
    return re.sub(pattern, new_word, string)

def cpp_compiler(code):
    code = code.replace("using", "\nusing")
    code = code.replace("\n", "\\n")
    code = code.replace("int    ", "\nint main")
    code = replace_word(code, "int", "\nint")
    code = replace_word(code, "void", "\nvoid")
    code = replace_word(code, "float", "\nfloat")
    code = replace_word(code, "double", "\ndouble")
    code = replace_word(code, "bool", "\nbool")


    # creates the environment for code execution
    process = subprocess.Popen(['g++', '-x', 'c++', '-o', 'code', '-'], stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    # runs the program to check for any errors that is not inside the code
    output, error = process.communicate(input=code.encode())
    if process.returncode != 0:
        # return self.output_formatting()
        return error.decode()
    else:
        # runs the code if there is no errors
        process = subprocess.Popen(['code'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   stdin=subprocess.DEVNULL)
        output, _ = process.communicate()
        # return self.output_formatting()
        return output.decode()


correct_codes = ["""#include <iostream> using namespace std;""",
        """#include <iostream> using namespace std; int main() { int num1, num2, sum; cout << "Enter two numbers: "; cin >> num1 >> num2; sum = num1 + num2; cout << "Sum of the numbers: " << sum << endl; return 0; }""",
        """#include <iostream> using namespace std; int main() { int year; cout << "Enter a year: "; cin >> year; if (year % 4 == 0) { if (year % 100 == 0) { if (year % 400 == 0) { cout << year << " is a leap year." << endl; } else { cout << year << " is not a leap year." << endl; } } else { cout << year << " is a leap year." << endl; } } else { cout << year << " is not a leap year." << endl; } return 0; }""",
        """#include <iostream> using namespace std; int main() { int num1, num2, temp; cout << "Enter two numbers: "; cin >> num1 >> num2; cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl; temp = num1; num1 = num2; num2 = temp; cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl; return 0; }""",
        """#include <iostream> using namespace std; int main() { int num1, num2; cout << "Enter two numbers: "; cin >> num1 >> num2; cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl; num1 = num1 + num2; num2 = num1 - num2; num1 = num1 - num2; cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl; return 0; }""",
        """#include <iostream> using namespace std; int main() { int num; cout << "Enter a number: "; cin >> num; cout << "Multiplication table for " << num << ":" << endl; for (int i = 1; i <= 10; i++) { cout << num << " x " << i << " = " << num*i << endl; } return 0; }""",
         "#include <iostream>\nint main() { int a = 11; std::cout << a / a << std::endl; return 0; }",
         "#include <iostream>\nint main() { int a - 12; std::cout << a % a << std::endl; return 0; }",
         "#include <iostream>\nint main() { int a = 13; int b = 14; std::cout << a + b << std::endl; return 0; }",
         "#include <iostream>\nint main() { int a = 15; int b = 16; std::cout << a - b << std::endl; return 0; }",
         "#include <iostream>\nint main() { int a = 17; int b = 18; std::cout << a * b << std::endl; return 0; }",
         "#include <iostream>\nint main() { int a = 19; int b = 20; std::cout << a / b << std::endl; return 0; }",
         "#include <iostream>\nint main() { int a = 21; int b = 22; std::cout << a % b << std::endl; return 0; }",
         "#include <iostream>\nint main() { int a = 23; if (a % 2 == 0) std::cout << \"even\" << std::endl; else std::cout << \"odd\" << std::endl; return 0; }",
         "#include <iostream>\nint main() { int a = 24; for (int i = 0; i < a; i++) std::cout << i << std::endl; return 0; }"
         ]

#
# def code_tester(code):
#     for i in code:
#         print(cpp_compiler(i))



print(cpp_compiler(correct_codes[0]))
# code_tester(correct_codes)