
import numpy as np

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    s = ''
    for i in range(b):
        s += chr(97 + i)
    for i in range(n - a * b):
        s += chr(97 + i % b)
    print(s)
