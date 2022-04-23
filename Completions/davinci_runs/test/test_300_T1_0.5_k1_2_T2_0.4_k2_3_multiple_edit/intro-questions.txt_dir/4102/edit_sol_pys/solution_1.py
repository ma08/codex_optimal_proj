import sys


def is_lucky_number(number):
    return len(number) % 2 == 0 and sum(int(digit) for digit in number[:len(number) // 2]) == sum(
        int(digit) for digit in number[len(number) // 2:])


def main():
    number = sys.stdin.readline().strip()
    if is_lucky_number(number):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
