

def main():
    a = float(input("Enter the first number: "))
    b = input("Enter the operation: ")
    c = float(input("Enter the second number: "))

    if b == "*":
        print(a*c)
    else:
        print(a + c)


if __name__ == "__main__":
    main()
