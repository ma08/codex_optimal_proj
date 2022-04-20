import math


a, b, t = map(int, input().split())

ans = math.floor(t / a) * b
print(int(ans))
