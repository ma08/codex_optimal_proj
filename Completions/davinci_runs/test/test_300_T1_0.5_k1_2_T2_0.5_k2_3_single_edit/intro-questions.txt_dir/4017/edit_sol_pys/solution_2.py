import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

def is_good(a):
    for i in range(len(a)):
        if a[i] == sum(a[:i]) + sum(a[i+1:]):
            return True
    return False

def solve(a):
    if is_good(a):
        return 1
    res = 0
    for i in range(len(a)):
        res += solve(a[:i] + a[i+1:])
    return res

print(solve(a))
