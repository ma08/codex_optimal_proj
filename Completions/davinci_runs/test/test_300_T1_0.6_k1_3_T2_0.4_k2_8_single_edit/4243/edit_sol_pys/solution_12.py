# coding: utf-8

from collections import defaultdict

def happiness(n):
    coins = [500, 100, 50, 10, 5, 1]
    d = defaultdict(lambda : 0)
    for coin in coins:
        d[coin] = n // coin
        n %= coin
    return 1000 * d[500] + 5 * d[5] + d[1]

n = int(input())
print(happiness(n))
