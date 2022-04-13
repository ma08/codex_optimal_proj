
def main():
    """
    1. Get input numbers
    2. Create a list of all numbers between them
    3. Filter out numbers that are not divisible by each of their digits
    4. Filter out numbers that have repeating digits
    5. Print the length of the list
    """
    low, high = map(int, input().split())
    numbers = list(range(low, high + 1))

    def is_divisible_by_digits(number):
        digits = [int(c) for c in str(number)]
        for d in digits:
            if d == 0 or number % d != 0:
                return False
        return True

    def has_repeats(number):
        digits = [int(c) for c in str(number)]
        return len(set(digits)) != len(digits)

    numbers = list(filter(is_divisible_by_digits, numbers))
    numbers = list(filter(has_repeats, numbers))
    print(len(numbers))

if __name__ == "__main__":
    main()
