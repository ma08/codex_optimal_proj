
def main():
    expression = input("Enter an expression: ")
    try:
        result = eval(expression)
        print("The result is:", result)
    except SyntaxError:
        print("The expression is invalid.")

if __name__ == "__main__":
    main()
