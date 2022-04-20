



def solution(n, k, prices):
    prices.sort()
    return sum(prices[:k])

import sys

n, k = [int(i) for i in sys.stdin.readline().split()]
prices = [int(i) for i in sys.stdin.readline().split()]

print(solution(n, k, prices))
