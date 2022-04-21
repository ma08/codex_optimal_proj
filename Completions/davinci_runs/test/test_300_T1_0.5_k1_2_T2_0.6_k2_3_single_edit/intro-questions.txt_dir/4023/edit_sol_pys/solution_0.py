import math

n = int(input())
a = list(map(float, input().split()))

print(math.ceil(sum(a) / max(a)))
