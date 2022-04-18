#!/usr/bin/env python3

n, x = map(int, input().split())
prices = list(map(int, input().split()))

prices.sort()

# If the smallest two elements are less than x, we can't mark anything
if prices[0] + prices[1] < x:
    print(0)
    exit()

# If the smallest two elements are greater than x, we can mark everything
if prices[0] + prices[1] > x:
    print(n)
    exit()

# Otherwise, we can mark everything except the smallest element
print(n - 1)
