import sys

n, k = [int(i) for i in sys.stdin.readline().split()]
prices = sorted([int(i) for i in sys.stdin.readline().split()])

print(sum(prices[:k]))
