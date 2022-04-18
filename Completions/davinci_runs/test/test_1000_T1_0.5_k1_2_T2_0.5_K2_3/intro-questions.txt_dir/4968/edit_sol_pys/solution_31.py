

import sys

[N, S, R] = map(int, sys.stdin.readline().split())
damaged = map(int, sys.stdin.readline().split())
reserve = map(int, sys.stdin.readline().split())

def check(reserve, damaged, N):
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
            elif i == N+1:
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
    return N - len(damaged)

print check(reserve, damaged, N+1)
