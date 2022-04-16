import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(m)]
ans = False
for i in range(n - m + 1):
    for j in range(n - m + 1):
        if a[i][j] == b[0][0]:
            for k in range(m):
                for l in range(m):
                    if a[i + k][j + l] != b[k][l]:
                        break
                else:
                    continue
                break
            else:
                ans = True
print("Yes" if ans else "No")
