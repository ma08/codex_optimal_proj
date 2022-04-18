

import sys

def main():
    year = int(sys.stdin.readline())
    if year % 26 in [2, 8, 14, 20]:
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()
