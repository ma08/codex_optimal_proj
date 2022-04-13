# -*- coding: utf-8 -*-

n, m = map(int, input().split())  # number of cups and max number of pages
a = list(map(int, input().split()))  # number of pages in each cup

a.sort()  # sort number of pages in ascending order

cups = 0  # number of cups already used
pages = 0  # number of pages already used
days = 0  # number of days needed

while cups < n:
    pages += a[cups]
    days += 1
    cups += 1
    if pages >= m:
        break
    if cups < n:
        pages -= days - 1

if pages < m:
    days = -1

print(days)
