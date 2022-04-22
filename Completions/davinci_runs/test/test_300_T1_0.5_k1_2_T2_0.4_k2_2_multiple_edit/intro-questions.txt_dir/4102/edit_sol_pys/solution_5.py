
import sys

def is_lucky_num(number):
    if len(number) % 2 == 0:
        half_len = len(number) // 2
        first_half = number[:half_len]
        second_half = number[half_len:]
        return sum(int(digit) for digit in first_half) == sum(int(digit) for digit in second_half)
    else:
        return False

def main():
    number = sys.stdin.readline().strip()
    if is_lucky_num(number):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
