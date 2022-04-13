

def main():
    a = int(input("Enter the first number: "))  # user input for first number
    b = input("Enter the operation: ")  # user input for operation
    c = int(input("Enter the second number: "))  # user input for second number

    if b == "*":  # if user inputs a *, then multiply
        print(a * c)
    else:
        print(a + c)  # if user inputs a +, then add


if __name__ == "__main__":
    main()
