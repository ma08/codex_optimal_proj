#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a, b, c = map(int, input().split())
order = input()

if order == "ABC":
    print(min(a, b, c), min(max(a, b), max(a, c)), max(max(a, b), c))
elif order == "ACB":
    print(min(a, b, c), max(min(a, b), min(b, c)), max(max(a, b), c))
elif order == "BAC":
    print(min(max(a, b), max(b, c)), min(a, b, c), max(max(a, b), c))
elif order == "BCA":
    print(min(max(a, b), max(b, c)), max(min(a, b), min(b, c)), max(max(a, b), c))
elif order == "CAB":
    print(max(a, b, c), min(a, b, c), min(max(a, b), c))
elif order == "CBA":
    print(max(a, b, c), min(max(a, b), c), min(a, b, c))
