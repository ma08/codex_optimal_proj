
import sys

[N, S, R] = map(int, sys.stdin.readline().split())
damaged = map(int, sys.stdin.readline().split())
reserve = map(int, sys.stdin.readline().split())

def check(reserve, damaged):
    for i in list(damaged):
        if i - 1 in reserve:
            reserve.remove(i - 1)
            damaged.remove(i)
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            damaged.remove(i)
    return len(list(damaged))

print check(reserve, damaged)
