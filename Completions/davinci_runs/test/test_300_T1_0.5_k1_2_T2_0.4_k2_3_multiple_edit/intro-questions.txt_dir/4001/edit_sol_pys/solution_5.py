#!/usr/bin/python3

N = int(input())
divisors = list(map(int, input().split()))
x = 1
y = 1
for i in range(0, N, 2):
    x *= divisors[i]
for i in range(1, N, 2):
    y *= divisors[i]
print(x, y)
