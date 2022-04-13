

import sys, math

def main():
    n, x, y = list(map(int, sys.stdin.readline().split()))
    a = list(map(int, sys.stdin.readline().split()))

    # if y >= 2 * x, then Slavik will always win
    if y >= 2 * x:
        print(0)
        return

    # if y >= 2 * x, then Slavik will always win
    if y >= 2 * x:
        print(0)
        return

    # if x < y < 2 * x, then Slavik will win if and only if the sum of the initial durabilities is odd
    if sum(a) % 2 == 0:
        print(0)
    else:
        print(1)

if __name__ == "__main__":
    main()
