

import sys

def main():
    year = int(sys.stdin.readline())
    if year % 26 == 1 or year % 26 == 7 or year % 26 == 13 or year % 26 == 19:
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()
