
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

def solve(i, m):
    if m == 0:
        return True
    if i >= n:
        return False
    res = solve(i+1, m) or solve(i+1, m-a[i])
    return res

if solve(0, m):
    print('yes')
else:
    print('no')
