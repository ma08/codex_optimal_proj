import math

x, k, d = map(int,input().split())

if k*d > abs(x):
    print(abs(x) - k*d)
else:
    print(abs(x - k*d))
