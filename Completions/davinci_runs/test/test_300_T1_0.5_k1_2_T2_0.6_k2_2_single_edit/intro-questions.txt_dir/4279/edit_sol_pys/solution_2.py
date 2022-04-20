
import math


def get_digits(n):
    return [int(i) for i in str(n)]


def is_lucky(n):
    digits = get_digits(n)
    for i in digits:
        if i != 4 and i != 7:
            return False
    return True


def is_lucky_or_almost(n):
    if is_lucky(n):
        return True

    digits = get_digits(n)
    for i in range(len(digits)):
        if digits[i] == 4 or digits[i] == 7:
            continue
        if is_lucky(n - digits[i]):
            return True

    return False


def main():
    n = int(input())
    print("YES" if is_lucky_or_almost(n) else "NO")


main()
