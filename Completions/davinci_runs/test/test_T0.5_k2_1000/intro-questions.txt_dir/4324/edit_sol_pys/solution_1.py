
import numpy as np

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    if a == 1:
        print(chr(97) * n)
    else:
        s = ""
        for i in range(b):
            s += chr(97 + i)
        for i in range(n - a * b):
            s += chr(97 + i % b)
        print(s)
