
import sys

def main():
    year = int(sys.stdin.readline())
    if year % 26 == 2 or year % 26 == 8 or year % 26 == 14 or year % 26 == 20:  # check if the year is divisible by 26 and if it is then check if it is divisible by 2,8,14,or 20
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()
