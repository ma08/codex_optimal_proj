
import sys
N, M = list(map(int, sys.stdin.readline().split()))
l = []
for i in range(N):
    l.append(list(map(int, sys.stdin.readline().split())))

l.sort(key=lambda x: x[0])
ans = 0
for i in range(M):
    if l[i][1] == 1:
        ans += l[i][0]
    else:
        ans += l[i][0]//2

print(ans)
