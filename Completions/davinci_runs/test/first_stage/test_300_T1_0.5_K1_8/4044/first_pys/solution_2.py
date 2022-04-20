

import sys

def main():
    a, b, x = map(int, sys.stdin.readline().split())

    if a < b:
        a, b = b, a

    if x < a:
        print("0" * x + "1" * (a - x) + "0" * b)
    else:
        print("1" * (a - (x - a)) + "0" * (x - a) + "1" * b)

if __name__ == "__main__":
    main()