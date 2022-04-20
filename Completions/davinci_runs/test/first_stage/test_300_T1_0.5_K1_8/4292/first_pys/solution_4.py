

from sys import stdin

num_fruits, num_kinds = map(int, stdin.readline().split())
prices = list(map(int, stdin.readline().split()))

prices.sort()
print(sum(prices[:num_kinds]))