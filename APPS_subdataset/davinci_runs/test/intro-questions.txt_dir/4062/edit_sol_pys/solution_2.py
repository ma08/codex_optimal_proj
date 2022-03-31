#!/usr/bin/env python3

a, b, c, d = list(map(int, input().split()))
print(max(a*c, a*d, b*c, b*d))
