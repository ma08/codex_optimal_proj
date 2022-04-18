#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))

count = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        count += A[i] * A[j]

print(count % (10 ** 9 + 7))  # 10 ** 9 + 7 は 10 ** 9 + 7 と表記する
