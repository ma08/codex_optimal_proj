

import sys

n, k = [int(i) for i in sys.stdin.readline().split()]
prices = [int(i) for i in sys.stdin.readline().split()]
prices.sort(reverse=True)

print(sum(prices[:k]))
