

import sys

def is_launch_window(year):
    if year % 26 == 2 or year % 26 == 5:
        return "yes"
    else:
        return "no"

def main():
    year = int(sys.stdin.readline())
    print(is_launch_window(year))

if __name__ == "__main__":
    main()
