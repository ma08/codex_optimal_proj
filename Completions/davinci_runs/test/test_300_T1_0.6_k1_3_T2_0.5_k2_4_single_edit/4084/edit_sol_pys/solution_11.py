#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# n, a, b = map(int, input().split())
# n -= 1


# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# gcd = gcd(a, b)

gcd = gcd(a, b)

print(n // (a + b) * a + min(n % (a + b), a))
