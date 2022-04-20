

import sys

def is_lucky_number(number):
    half_len = len(number) // 2
    first_half = number[:half_len]
    second_half = number[half_len:]
    if sum(int(digit) for digit in first_half) == sum(int(digit) for digit in second_half):
        return True
    else:

def is_even(number):
    if len(number) % 2 == 0:
        return True
    else:
        return False

def is_lucky(number):
    if is_even(number):
        if is_lucky_number(number):
            return True
        else:
            return False
    else:
        return False

        return False

def main():
    number = sys.stdin.readline().strip()
    if is_lucky(number):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
