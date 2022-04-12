import sys

def is_lucky_number(n):
    if len(n) % 2 == 0:
        half_len = len(n) // 2
        first_half = n[:half_len]
        second_half = n[half_len:]
        return sum(int(digit) for digit in first_half) == sum(int(digit) for digit in second_half)
    return False

def main():
    n = sys.stdin.readline().strip()
    if is_lucky_number(n):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
