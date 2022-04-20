
import math

A, B, X = list(map(int, input().split()))
if B > X:
    print(0) if A + B > X else print(1)
elif A + B > X:
    print(0) if A + B > X else print(1)
elif A + B < X:
    print(10**9) if A + B < X else print(10**9-1)
