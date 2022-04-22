import sys

def is_lucky_num(number):
    if len(number) % 2 == 0:
        half_len = len(number) // 2
        first_half = int(number[:half_len])
        second_half = int(number[half_len:])
        if first_half == second_half:
            return True
        else:
            return False
    else:
        return False

def main():
    number = sys.stdin.readline().strip() # read line from input
    if is_lucky_num(number):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
