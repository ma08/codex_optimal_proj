

import sys

def is_launch_win(year):
    if year % 4 == 0:
        print("yes")
    else:
        print("no")

def main():
    year = int(sys.stdin.readline())
    is_launch_win(year)

if __name__ == "__main__":
    main()
