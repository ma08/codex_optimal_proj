import sys


n, X = map(int, sys.stdin.readline().split())
prices = list(map(int, sys.stdin.readline().split()))

prices.sort()

count = 0

for i in range(n):
    for j in range(i+1, n):
        if prices[i] + prices[j] > X:
            count += 1

print(count)
