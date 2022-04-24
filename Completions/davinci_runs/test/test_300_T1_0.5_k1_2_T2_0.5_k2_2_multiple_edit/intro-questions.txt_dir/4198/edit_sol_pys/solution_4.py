import math
N, A, B = list(map(int, input().split()))


if A + B > N:
    print(0)
else:
    upper = N - B
    lower = 1
    while lower < upper:
        mid = math.ceil((upper + lower) / 2)
        if A * mid + B * len(str(mid)) <= X:
            lower = mid + 1
        else:
            upper = mid - 1

    print(lower - 1)
