

import sys

def main():
    n = int(sys.stdin.readline())
    if n > 0:
        print("positive")
    elif n == 0:
        print("zero")
    else:
        print("safe")

if __name__ == '__main__':
    main()
