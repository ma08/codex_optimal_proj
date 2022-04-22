
import sys

def is_lucky_number(number):
    number = str(number)
    half_len = len(number) // 2
    first_half = number[:half_len]
    second_half = number[half_len:]
    if sum(int(digit) for digit in first_half) == sum(int(digit) for digit in second_half):
        return True
    else:


def is_lucky_number_v2(number):
    number = str(number)
    if len(number) % 2 == 0:
        return is_lucky_number(number)
    else:
        return False

        return False

def main():
    number = sys.stdin.readline().strip()
    if is_lucky_number(number):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
