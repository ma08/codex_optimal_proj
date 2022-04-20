

from sys import stdin

n, x = map(int, stdin.readline().split())
li = list(map(int, stdin.readline().split()))

ans = 0
for i, l in enumerate(li):
    if x - l >= 0:
        ans += 1
        x -= l
    else:
        break
print(ans)