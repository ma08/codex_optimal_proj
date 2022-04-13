

def main():
    # Get input number
    # Create a list of all number between them
    low, high = map(int, input().split())
    numbers = list(range(low, high + 1))
    # Filter out number that are not divisible by each of their digits

    def is_divisible(number):
        digits = [int(c) for c in str(number)]
        for d in digits:
            if d == 0 or number % d != 0:
                return False
        return True

    # Filter out number that have repeating digits
    def has_repeats(number):
        digits = [int(c) for c in str(number)]
        return len(set(digits)) != len(digits)

    # Print the length of the number
    numbers = list(filter(is_divisible, numbers))
    numbers = list(filter(has_repeats, numbers))
    print(len(numbers))

if __name__ == "__main__":
    main()
