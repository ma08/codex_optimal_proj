

import sys

[N, S, R] = map(int, sys.stdin.readline().split())
damaged = map(int, sys.stdin.readline().split())
reserve = map(int, sys.stdin.readline().split())

def check(reserve, damaged):
    for i in damaged:
        if i-1 in reserve:
            reserve.remove(i - 1)
            damaged.remove(i)
        if i+1 in reserve:
            reserve.remove(i + 1)
            damaged.remove(i)
    return len(damaged)

print check(reserve, damaged)
