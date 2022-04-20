
import re

def main():
    expression = input("Enter an expression: ")
    if re.match("^\d+$", expression):
        print(expression)
    elif re.match("^\d+[+-/*]\d+$", expression):
        result = eval(expression)
        print(result)
    else:
        print("Invalid expression")

if __name__ == "__main__":
    main()
