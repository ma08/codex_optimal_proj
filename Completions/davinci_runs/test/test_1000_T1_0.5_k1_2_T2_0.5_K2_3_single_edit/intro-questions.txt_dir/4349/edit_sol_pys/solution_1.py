#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n, m = map(int, input().split())
k = list(map(int, input().split()))

sales = set()

for _ in range(m):
    d, t = map(int, input().split())
    sales.add((d, t))

days = 0
for i in range(n):
    if k[i] > 0:
        on_sale = [d for d, t in sales if t == i+1]
        if len(on_sale) == 0:
            days += 2 * k[i]
        else:
            days += 1
            k[i] -= 1
            for day in on_sale:
                if k[i] > 0:
                    days += 1
                    k[i] -= 1
                else:
                    break
            if k[i] > 0:
                days += 2 * k[i]
print(days)
