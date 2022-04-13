def main():
    # Get input
    x, a, b = map(int, input().split())
    # Calculate
    remainder = (x - a) % b
    # Print
    print(remainder)


if __name__ == '__main__':
    main()
