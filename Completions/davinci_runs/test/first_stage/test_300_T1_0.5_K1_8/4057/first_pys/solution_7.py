

import sys

def min_pockets(coins):
    coins.sort()
    n = len(coins)
    pockets = 0
    i = 0
    while i < n:
        pockets += 1
        j = i + 1
        while j < n and coins[j] == coins[i]:
            j += 1
        i = j
    return pockets

n = int(sys.stdin.readline())
coins = [int(x) for x in sys.stdin.readline().split()]
print(min_pockets(coins))