
import sys
sys.setrecursionlimit(10**6)
# Solution

H, n = map(int, input().split())
d = list(map(int, input().split()))

def dfs(i, hp):
    if hp <= 0:
        return i
    if i >= n:
        return -1
    return dfs(i+1, hp+d[i])

for i in range(n):
    hp += d[i]
    minute += 1
    if hp <= 0:
        print(minute)
        break
else:
    print(-1)
