

def is_lucky(n):
    """Determine if a number is a lucky number.

    A number is a lucky number if the sum of its digits is divisible by 8.

    Args:
        n (int): Number to check.

    Returns:
        int: 0 if n is not a lucky number, 1 if n is a lucky number.
    """
    return sum(map(int, str(n))) % 8 == 0

def main():
    print(is_lucky(int(input())))

if __name__ == "__main__":
    main()