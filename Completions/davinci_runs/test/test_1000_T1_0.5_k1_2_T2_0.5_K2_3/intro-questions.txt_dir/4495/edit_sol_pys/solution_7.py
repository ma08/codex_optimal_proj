import math

A, B, X = map(int, input().split())

if A % X == 0:
    print(math.floor(B/X) - math.floor(A/X) + 1)
else:
    print(math.floor(B/X) - math.floor(A/X))
