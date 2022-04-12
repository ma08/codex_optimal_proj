


def main():
    a = int(input("Enter the first number: "))  # input first number
    b = input("Enter the operation: ")  # input operation
    c = int(input("Enter the second number: "))  # input second number

    if b == "*":  # if operation is multiplication
        print(a*c)
    else:  # if operation is addition
        print(a+c)


if __name__ == "__main__":
    main()
