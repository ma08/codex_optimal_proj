

def main():
    a = int(input("Enter the first number: "))  # noqa
    b = input("Enter the operation: ")
    c = int(input("Enter the second number: "))  # noqa

    if b == "*":
        print(a * c)
    else:
        print(a + c)


if __name__ == "__main__":
    main()
