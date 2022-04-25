import math
A, B, X = list(map(int, input().split()))

upper = 10 ** 9 + 1
lower = 0
while lower <= upper:
    mid = math.floor((upper + lower) / 2)
    if A * mid + B * len(str(mid)) <= X:
        lower = mid + 1
    else:
        upper = mid - 1

    print(lower - 1)
