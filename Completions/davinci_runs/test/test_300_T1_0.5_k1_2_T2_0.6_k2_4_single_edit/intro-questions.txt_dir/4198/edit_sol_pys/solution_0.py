

import math

A, B, X = list(map(int, input().split()))

if A + B > X:
    print(0)

else:
    upper = X - B
    lower = 1
    while lower <= upper:
        mid = int((upper + lower) / 2)
        if A * mid + B * len(str(mid)) <= X:
            lower = mid + 1
        else:
            upper = mid - 1

    print(lower - 1)
