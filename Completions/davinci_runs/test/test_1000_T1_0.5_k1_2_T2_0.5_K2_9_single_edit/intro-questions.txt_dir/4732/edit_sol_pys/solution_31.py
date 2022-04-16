


def add(a, b):
    print(a + b)


def multiply(a, b):
    print(a * b)



def main():
    a = int(input("Enter the first number: "))
    b = input("Enter the operation: ")
    c = int(input("Enter the second number: "))

    if b == "+":
        add(a, c)
    else:
        multiply(a, c)


if __name__ == "__main__":
    main()
