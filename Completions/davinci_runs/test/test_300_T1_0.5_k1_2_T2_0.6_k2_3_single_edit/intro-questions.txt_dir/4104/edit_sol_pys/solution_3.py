

def main():
    expression = input("Enter an expression: ")
    try:
        result = eval(expression)
        print("Answer: ", result)
    except:
        print("Invalid Input")

if __name__ == "__main__":
    main()
