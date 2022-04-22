
import sys


def is_lucky(number):
    if len(number) % 2:
        return False

    half_len = len(number) // 2
    first_half = number[:half_len]
    second_half = number[half_len:]
    return sum(int(digit) for digit in first_half) == sum(int(digit) for digit in second_half)


def main():
    number = sys.stdin.readline().strip()
    if is_lucky(number):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
