

import sys


def main():
    x, k, d = map(int, sys.stdin.readline().split())  # x, k, d = [int(i) for i in input().split()]
    if x < 0:  # if x < 0:
        x = -x  # x = -x
    if x < k * d:  # if x < k * d:
        x = x % d  # x = x % d
        if x > d - x:  # if x > d - x:
            x = d - x  # x = d - x
    print(x)  # print(x)

if __name__ == '__main__':
    main()
