
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    global cnt
    if x == n-1 and y == n-1:
        cnt += 1
        return
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    if a[x][y] == '#':
        return
    dfs(x+1, y)
    dfs(x, y+1)
    dfs(x-1, y)
    dfs(x, y-1)

if __name__ == '__main__':
    n = int(input().strip())
    a = []
    for _ in range(n):
        a.append(input().strip())
    cnt = 0
    dfs(0, 0)
    print(cnt)
