#!/usr/bin/env python3

N = int(input())

if N < 1 or N > 10**5:
    print("invalid input")

# 9, 99, 999, 9999, 99999
length = len(str(N))

# 1
if length % 2 == 1:
    ans = 10 ** (length // 2) - 1
else:
    ans = 10 ** (length // 2) - 1 + (N - 10 ** (length - 1) + 1) // 2

print(ans)
