import math

n, x, t = map(int, input().split())

print(t * math.ceil(n / x))
