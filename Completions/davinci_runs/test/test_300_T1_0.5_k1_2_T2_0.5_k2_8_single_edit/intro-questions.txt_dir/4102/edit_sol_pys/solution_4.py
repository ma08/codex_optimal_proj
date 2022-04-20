
import sys

def is_lucky_number(number):
    if len(number) % 2 == 0 and len(number) > 0:
        half_len = len(number) // 2
        first_half = number[:half_len]
        second_half = number[half_len:]
        if sum(int(digit) for digit in first_half) == sum(int(digit) for digit in second_half) and len(first_half) > 0 and len(second_half) > 0:
            return True
        else:
            return False
    else:
        return False
    
def main():
    number = sys.stdin.readline().strip()
    if is_lucky_number(number):
        print("Yes")
    else:
        print("No")
    
if __name__ == "__main__":
    main()
