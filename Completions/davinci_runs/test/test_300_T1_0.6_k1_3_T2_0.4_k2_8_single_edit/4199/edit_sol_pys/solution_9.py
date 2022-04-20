import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
q = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))


def dfs(i, sum):
    if i == n:
        return sum == 0
    if dfs(i + 1, sum):
        return True
    if dfs(i + 1, sum - a[i]):
        return True
    return False


for i in m:
    if dfs(0, i):
        print('yes')
    else:
        print('no')
