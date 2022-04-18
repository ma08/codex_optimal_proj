

# Solution 1
import sys
raw_input = sys.stdin.readline

n, X = map(int, raw_input().split())
prices = list(map(int, raw_input().split()))

prices.sort()

count = 0
for i in range(n):
    if prices[i] >= X:
        break
    for j in range(i + 1, n):
        if prices[i] + prices[j] > X:
            count += 1

print(n - count)

# Solution 2
import sys
raw_input = sys.stdin.readline

n, X = map(int, raw_input().split())
prices = list(map(int, raw_input().split()))

prices.sort()

count = 0
for i in range(n):
    if prices[i] >= X:
        break
    for j in range(i + 1, n):
        if prices[i] + prices[j] > X:
            count += 1

print(n - count)
