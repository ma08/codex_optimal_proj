import sys

n, k = [int(i) for i in input().split()]
prices = [int(i) for i in input().split()]
prices.sort(reverse=True)

print(sum(prices[:k]))
