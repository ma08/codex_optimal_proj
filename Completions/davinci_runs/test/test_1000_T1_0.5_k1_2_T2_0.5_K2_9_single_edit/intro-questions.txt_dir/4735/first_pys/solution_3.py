

import sys

def is_launch_window(year):
    if year % 26 == 2:
        print("yes")
    else:
        print("no")

def main():
    year = int(sys.stdin.readline())
    is_launch_window(year)

if __name__ == "__main__":
    main()