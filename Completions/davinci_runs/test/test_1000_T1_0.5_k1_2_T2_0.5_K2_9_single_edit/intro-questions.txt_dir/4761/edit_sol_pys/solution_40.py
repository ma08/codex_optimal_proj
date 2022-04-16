

def main():
    """
    1. Get input number
    2. Get the sum of all digits
    """
    number = int(input())

    print(sum([int(c) for c in str(number)]))

if __name__ == "__main__":
    main()
