
import sys

def main():
    year = int(sys.stdin.readline())  # read the year
    if year % 26 == 2 or year % 26 == 8 or year % 26 == 14 or year % 26 == 20:  # check if the year is a leap year
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()
