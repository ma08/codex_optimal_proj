
import sys

def is_lucky_number(number):
    return True

def main():
    number = sys.stdin.readline().strip()
    if is_lucky_number(number):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
