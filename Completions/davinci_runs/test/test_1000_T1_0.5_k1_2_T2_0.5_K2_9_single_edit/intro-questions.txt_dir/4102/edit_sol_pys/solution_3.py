
import sys

def is_lucky_number(number_string):
    half_len = len(number_string) // 2
    first_half = number_string[:half_len]
    second_half = number_string[half_len:]
    return sum(int(digit) for digit in first_half) == sum(int(digit) for digit in second_half)

def main():
    number_string = sys.stdin.readline().strip()
    if is_lucky_number(number_string):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
