

def main():
    # Read inputs
    a = int(input())
    op = input()
    b = int(input())

    # Print output
    if op == '+':
        print(a + b)
    elif op == '*':
        print(a * b)

if __name__ == '__main__':
    main()
