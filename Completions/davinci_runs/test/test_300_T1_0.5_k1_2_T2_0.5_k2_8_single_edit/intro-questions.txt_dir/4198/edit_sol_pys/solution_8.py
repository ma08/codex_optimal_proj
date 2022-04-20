
import math

A, B, X = list(map(int, input().split()))

if A + B > X or A * 10 ** 9 + B * len(str(10 ** 9)) < X:
    print(0)

else:
    upper = 10 ** 9
    lower = 1
    while lower <= upper:
        mid = math.floor((upper + lower) / 2)
        if A * mid + B * len(str(mid)) <= X:
            lower = mid + 1
        else:
            upper = mid - 1

    print(lower - 1)
