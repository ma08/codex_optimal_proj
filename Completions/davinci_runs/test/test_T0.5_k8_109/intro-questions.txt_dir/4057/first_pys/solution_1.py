

import sys

def main():
    n = int(sys.stdin.readline())
    coins = map(int, sys.stdin.readline().split())
    # print n, coins

    coins.sort()
    # print coins

    pockets = [coins[0]]
    for i in range(1, n):
        if coins[i] != coins[i-1]:
            pockets.append(coins[i])

    print len(pockets)

if __name__ == '__main__':
    main()