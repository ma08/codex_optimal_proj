


def main():
    # Get input
    x = int(input())
    a = int(input())
    b = int(input())
    # Calculate
    remainder = x - a - (x - a) // b * b
    # Print output
    print(remainder)


if __name__ == '__main__':
    main()
