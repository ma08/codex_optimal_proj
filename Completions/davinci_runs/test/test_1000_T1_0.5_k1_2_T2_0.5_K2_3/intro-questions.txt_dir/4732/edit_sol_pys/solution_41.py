

def main():
    a = int(input("Enter the first number: "))
    b = input("Enter the operation: ")
    c = int(input("Enter the second number: "))

    if b == "*":
        print(a*c)
    else:
        print(a+c)


if __name__ == "__main__":
    main()
