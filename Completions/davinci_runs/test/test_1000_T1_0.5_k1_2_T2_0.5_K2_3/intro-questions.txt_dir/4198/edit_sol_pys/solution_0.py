

import math

A, B, X = list(map(int, input().split()))

if A + B > X:
    print(0)

else:
    upper = 10 ** 9
    lower = 1
    while lower < upper:
        mid = math.ceil((upper + lower) / 2)
        if A * mid + B * len(str(mid)) <= X:
            lower = mid
        else:
            upper = mid

    print(lower)
