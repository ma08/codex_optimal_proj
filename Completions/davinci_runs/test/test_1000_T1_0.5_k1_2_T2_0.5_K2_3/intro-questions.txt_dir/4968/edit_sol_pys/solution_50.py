
import sys

[N, S, R] = map(int, sys.stdin.readline().split())
damaged = list(map(int, sys.stdin.readline().split()))
reserve = list(map(int, sys.stdin.readline().split()))

for i in damaged:
    if i-1 in reserve:
        reserve.remove(i-1)
        damaged.remove(i)
    elif i+1 in reserve:
        reserve.remove(i+1)
        damaged.remove(i)
    else:
        if i in reserve:
            reserve.remove(i)
            damaged.remove(i)
        elif i == N:
            reserve.remove(i-1)
            damaged.remove(i)
        elif i == 1:
            reserve.remove(i+1)
            damaged.remove(i)
        else:
            if i-1 in reserve:
                reserve.remove(i-1)
                damaged.remove(i)
            elif i+1 in reserve:
                reserve.remove(i+1)
                damaged.remove(i)

print(N - len(damaged))
