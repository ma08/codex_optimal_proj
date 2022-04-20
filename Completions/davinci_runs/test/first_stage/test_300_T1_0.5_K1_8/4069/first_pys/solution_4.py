
import math

x, k, d = map(int, input().split())

if k * d < abs(x):
    print(abs(x) - k * d)
else:
    if math.ceil(abs(x) / d) % 2 == k % 2:
        print(abs(x) % d)
    else:
        print(d - (abs(x) % d))