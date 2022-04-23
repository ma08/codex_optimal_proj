
import sys

def is_lucky_number(num):
    if len(num) % 2 == 0 and len(num) != 0:
        half_len = len(num) // 2
        first_half = num[:half_len]
        second_half = num[half_len:]
        if sum(int(digit) for digit in first_half) == sum(int(digit) for digit in second_half): 
            return True
        else:
            return False
    else:
        return False

def main():
    num = sys.stdin.readline().strip()
    if is_lucky_number(num):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
