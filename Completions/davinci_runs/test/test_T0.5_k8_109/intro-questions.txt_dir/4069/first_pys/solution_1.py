

import sys

def main():
    x, k, d = map(int, sys.stdin.readline().rstrip().split())
    if x < 0:
        x = -x
    if k < x // d:
        print(x - k * d)
    else:
        x -= k * d
        k -= x // d
        if k % 2 == 0:
            print(x % d)
        else:
            print(d - x % d)

if __name__ == "__main__":
    main()