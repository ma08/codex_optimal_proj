
import math

A, B, X = list(map(int, input().split()))

if A + B > X:
    print(0)

else:
    upper = math.floor(X / A)
    lower = 0
    if B > X:
        print(0)
    else:
        while lower <= upper:
            mid = math.floor((upper + lower) / 2)
            if A * mid + B * len(str(mid)) <= X:
                lower = mid + 1
            else:
                upper = mid - 1
        print(lower - 1)
