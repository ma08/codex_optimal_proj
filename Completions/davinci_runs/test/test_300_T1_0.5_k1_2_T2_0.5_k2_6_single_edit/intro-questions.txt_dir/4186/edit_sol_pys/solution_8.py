import sys


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

ans = 0
for i in d:
    ans += d[i] - 2

print(ans)
