
import math

A, B, X = map(int, input().split())

if A + B > X or A * 1000000000 + B * 10 < X:
    print(0)

else:
    upper = 10 ** 9
    lower = 1
    while lower < upper:
        mid = (upper + lower) // 2
        if A * mid + B * len(str(mid)) < X:
            lower = mid + 1
        else:
            upper = mid - 1

    print(lower - 1)
