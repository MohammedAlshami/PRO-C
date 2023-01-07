import concurrent.futures
import subprocess #for python compiler
import os
import threading
mutex = threading.Lock()



correct_codes = ["""#include <iostream>using namespace std;\n int main() { cout << "Hello, World!" << endl; return 0; }""",
        """#include <iostream> using namespace std; int main() { int num1, num2, sum; cout << "Enter two numbers: "; cin >> num1 >> num2; sum = num1 + num2; cout << "Sum of the numbers: " << sum << endl; return 0; }""",
        """#include <iostream> using namespace std; int main() { int year; cout << "Enter a year: "; cin >> year; if (year % 4 == 0) { if (year % 100 == 0) { if (year % 400 == 0) { cout << year << " is a leap year." << endl; } else { cout << year << " is not a leap year." << endl; } } else { cout << year << " is a leap year." << endl; } } else { cout << year << " is not a leap year." << endl; } return 0; }""",
        """#include <iostream> using namespace std; int main() { int num1, num2, temp; cout << "Enter two numbers: "; cin >> num1 >> num2; cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl; temp = num1; num1 = num2; num2 = temp; cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl; return 0; }""",
        """#include <iostream> using namespace std; int main() { int num1, num2; cout << "Enter two numbers: "; cin >> num1 >> num2; cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl; num1 = num1 + num2; num2 = num1 - num2; num1 = num1 - num2; cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl; return 0; }""",
        """#include <iostream> using namespace std; int main() { int num; cout << "Enter a number: "; cin >> num; cout << "Multiplication table for " << num << ":" << endl; for (int i = 1; i <= 10; i++) { cout << num << " x " << i << " = " << num*i << endl; } return 0; }""",
         "#include <iostream>\nint main() { int a = 11; std::cout << a / a << std::endl; return 0; }",
         "#include <iostream>\nint main() { int a = 12; std::cout << a % a << std::endl; return 0; }",
         "#include <iostream>\nint main() { int a = 13; int b = 14; std::cout << a + b << std::endl; return 0; }",
         "#include <iostream>\nint main() { int a = 15; int b = 16; std::cout << a - b << std::endl; return 0; }",
         "#include <iostream>\nint main() { int a = 17; int b = 18; std::cout << a * b << std::endl; return 0; }",
         "#include <iostream>\nint main() { int a = 19; int b = 20; std::cout << a / b << std::endl; return 0; }",
         "#include <iostream>\nint main() { int a = 21; int b = 22; std::cout << a % b << std::endl; return 0; }",
         "#include <iostream>\nint main() { int a = 23; if (a % 2 == 0) std::cout << \"even\" << std::endl; else std::cout << \"odd\" << std::endl; return 0; }",
         "#include <iostream>\nint main() { int a = 24; for (int i = 0; i < a; i++) std::cout << i << std::endl; return 0; }"
         ]

count = 0
def cpp_compiler(code):
    global count
    count += 1
    code = code.replace("using", "\nusing")
    code = code.replace("int main", "\nint main")
    code = code.replace("void main", "\nvoid main")

    # creates the environment for code execution
    with mutex:
        process = subprocess.Popen(['g++', '-x', 'c++', '-o', f'code', '-'], stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

    # runs the program to check for any errors that is not inside the code
    output, error = process.communicate(input=code.encode())
    if process.returncode != 0:
        print(error.decode())
        return None
    else:
        # runs the code if there is no errors
        with mutex:
            process = subprocess.Popen([f'code'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.DEVNULL)
        output, _ = process.communicate()
        return output.decode()



def main():
    # Make sure the map and function are working
    # print([val for val in map(f, nums)])

    # Test to make sure concurrent map is working
    with concurrent.futures.ProcessPoolExecutor() as executor:
        print([val * 2 for val in executor.map(cpp_compiler, correct_codes[:2])])

if __name__ == '__main__':
    main()

# print(x)

