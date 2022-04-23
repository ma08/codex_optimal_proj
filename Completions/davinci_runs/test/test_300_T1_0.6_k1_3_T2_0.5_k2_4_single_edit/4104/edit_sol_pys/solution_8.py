

import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def main(argv):
    if len(argv) == 4:
        operation = argv[1]
        x = int(argv[2])
        y = int(argv[3])
        if operation == '+':
            print(add(x, y))
        elif operation == '-':
            print(subtract(x, y))
        elif operation == '*':
            print(multiply(x, y))
        elif operation == '/':
            print(divide(x, y))
        else:
            print("Invalid operator")
            sys.exit(1)
    else:
        print("Usage: calc.py <operator> <x> <y>")
        sys.exit(1)

if __name__ == '__main__':
    main(sys.argv)
