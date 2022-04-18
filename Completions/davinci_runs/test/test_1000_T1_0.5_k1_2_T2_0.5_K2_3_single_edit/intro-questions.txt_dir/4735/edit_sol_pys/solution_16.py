

import sys

def is_launch_window(year, month):
    if year % 26 == 2 and month == "OCT":
        return "yes"
    else:
        return "no"

def main():
    year = sys.stdin.readline().strip()
    month = sys.stdin.readline().strip()
    print(is_launch_window(int(year), month))

if __name__ == "__main__":
    main()
