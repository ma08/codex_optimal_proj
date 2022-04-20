#!/usr/bin/env python3

n = int(input())
s = input()

def reverse(str, start, end):
    return str[:start] + str[start:end][::-1] + str[end:]

for i in range(n, 0, -1):
    if n % i == 0:
        s = reverse(s, 0, i)

print(s)
