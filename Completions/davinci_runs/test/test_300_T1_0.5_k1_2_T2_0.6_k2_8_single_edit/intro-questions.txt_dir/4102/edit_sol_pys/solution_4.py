
import sys

def is_lucky_number(number):
    half_len = len(number) // 2
    first_half = number[:half_len]
    second_half = number[half_len:]
    return sum(int(digit) for digit in first_half) == sum(int(digit) for digit in second_half)

def main():
    number = sys.stdin.readline().strip()
    print("Yes" if is_lucky_number(number) else "No")

if __name__ == "__main__":
    main()
