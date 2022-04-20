

import sys

def main():
    x, y = map(int, sys.stdin.readline().split())
    if x >= 30 and y >= 30:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
