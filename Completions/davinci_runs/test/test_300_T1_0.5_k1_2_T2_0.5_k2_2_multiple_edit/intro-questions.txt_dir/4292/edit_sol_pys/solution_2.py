

import sys

n, k = [int(i) for i in sys.stdin.readline().split()]
prices = [int(i) for i in sys.stdin.readline().split()]
# prices.sort()


min_sum = sum(prices[:k])

for i in range(len(prices) - k):
    min_sum = min(min_sum, sum(prices[i:i+k]))

print(min_sum)
