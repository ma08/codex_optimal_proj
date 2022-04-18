
import sys

[N, S, R] = map(int, sys.stdin.readline().split())
damaged = list(map(int, sys.stdin.readline().split()))
reserve = list(map(int, sys.stdin.readline().split()))

def check(reserve, damaged):
    for i in range(len(damaged)):
        if damaged[i]-1 in reserve:
            reserve.remove(damaged[i]-1)
            damaged.remove(damaged[i])
        elif damaged[i]+1 in reserve:
            reserve.remove(damaged[i]+1)
            damaged.remove(damaged[i])
    return len(damaged)

print check(reserve, damaged)
