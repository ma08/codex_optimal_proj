

import sys

def main():
    year = int(sys.stdin.readline()) - 1
    if year % 26 == 1 or year % 26 == 7 or year % 26 == 13 or year % 26 == 19 or year % 26 == 25:
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()
