import sys
import math



def main():
    x, k, d = map(int, sys.stdin.readline().strip().split())
    if abs(x) >= k * d:
        print(abs(x) - k * d)
    else:
        print(abs(x - (x // d) * d))


if __name__ == '__main__':
    main()
