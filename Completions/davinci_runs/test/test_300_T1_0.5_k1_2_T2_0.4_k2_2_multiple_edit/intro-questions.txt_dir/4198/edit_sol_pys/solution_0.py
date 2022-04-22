
import math

a, b, x = list(map(int, input().split()))

if a + b > x:
    print(0)
else:
    upper = x - b
    lower = 1
    while lower <= upper:
        mid = math.floor((upper + lower) / 2)
        if a * mid + b * len(str(mid)) <= x:
            lower = mid + 1
        else:
            upper = mid - 1

    print(lower - 1)
