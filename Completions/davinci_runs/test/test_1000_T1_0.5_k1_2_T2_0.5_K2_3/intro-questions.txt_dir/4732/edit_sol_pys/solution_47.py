

def main():
    a = int(input("Enter the first number: "))  # takes the first number
    b = input("Enter the operation: ")  # takes the operation
    c = int(input("Enter the second number: "))  # takes the second number

    if b == "*":  # checks if the operation is multiplication
        print(a*c)
    else:  # checks if the operation is addition
        print(a+c)


if __name__ == "__main__":  # checks if the file is being run
    main()
