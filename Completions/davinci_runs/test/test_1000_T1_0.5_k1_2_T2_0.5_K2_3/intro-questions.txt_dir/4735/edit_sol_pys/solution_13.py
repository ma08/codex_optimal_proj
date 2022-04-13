

import sys

def is_launch_window(year):
    if year % 26 == 0 or year % 26 == 2 or year % 26 == 4:
        print("yes")
    else:
        print("no")

def main():
    year = int(sys.stdin.readline().strip())
    is_launch_window(year)

if __name__ == "__main__":
    main()
