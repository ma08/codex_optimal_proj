

import sys

def main():
    n, X = list(map(int, sys.stdin.readline().split()))
    prices = sorted(list(map(int, sys.stdin.readline().split())))

    res = 0
    for i in range(n):
        if prices[i] > X:
            break
        res += 1
        X -= prices[i]
    print(res)

if __name__ == '__main__':
    main()
