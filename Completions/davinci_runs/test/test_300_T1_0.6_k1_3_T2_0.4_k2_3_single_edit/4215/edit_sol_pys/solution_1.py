#!/usr/bin/env python3

A, B = map(int, input().split())
print(A - B if B < A else 0)
