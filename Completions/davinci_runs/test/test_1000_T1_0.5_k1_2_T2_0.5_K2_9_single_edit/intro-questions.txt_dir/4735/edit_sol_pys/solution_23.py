

import sys

def main():
    year = int(sys.stdin.readline()) % 26
    if year == 2 or year == 8 or year == 14 or year == 20:
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()
