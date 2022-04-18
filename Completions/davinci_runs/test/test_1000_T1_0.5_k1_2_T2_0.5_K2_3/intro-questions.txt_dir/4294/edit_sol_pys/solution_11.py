

def main():
    # Read inputs
    a, b, c = [int(i) for i in input().split()]

    # Compare the two values and print the result.
    if a < b < c:
    elif a < c < b:
        print(10)
    elif b < a < c:
        print(10)
    elif b < c < a:
        print(10)
    elif c < a < b:
        print(10)
    elif c < b < a:
        print(10)
    else:
        print(0)

        print(0)
    else:
        print(10)

if __name__ == '__main__':
    main()
