def main():
    # Get input
    x = int(input()) # The number
    a = int(input()) # The first number
    b = int(input()) # The second number
    # Calculate
    remainder = x - a
    remainder = remainder - (remainder // b) * b
    # Print
    print(remainder)


if __name__ == '__main__':
    main()
