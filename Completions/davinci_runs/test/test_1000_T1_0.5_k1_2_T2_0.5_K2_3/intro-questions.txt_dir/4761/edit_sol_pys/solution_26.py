

def main():
    """
    1. Get input numbers
    2. Create a list of all numbers between them
    3. Filter out numbers that are not divisible by each of their digits.
    4. Filter out numbers that have repeating digits.
    5. Print the length of the list
    """
    low, high = map(int, input().split())
    numbers = list(range(low, high + 1))

    def is_divisible(n):
        digits = [int(c) for c in str(n)]
        return all([d != 0 and n % d == 0 for d in digits])

    def has_repeats(n):
        digits = [int(c) for c in str(n)]
        return len(digits) != len(set(digits))

    numbers = list(filter(is_divisible, numbers))
    numbers = list(filter(has_repeats, numbers))
    print(len(numbers))

if __name__ == "__main__":
    main()
