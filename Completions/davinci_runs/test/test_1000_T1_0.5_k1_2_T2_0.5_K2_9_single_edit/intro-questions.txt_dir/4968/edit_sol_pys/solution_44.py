
import sys

[N, S, R] = map(int, sys.stdin.readline().split())
damaged = map(int, sys.stdin.readline().split())
reserve = map(int, sys.stdin.readline().split())

def check(reserve, damaged, N):
    for i in range(N):
        if i+1 in damaged:
            if i in reserve or i+2 in reserve:
                reserve.remove(i)
                reserve.remove(i+2)
                damaged.remove(i+1)
    return len(damaged), reserve, damaged

print check(reserve, damaged)
