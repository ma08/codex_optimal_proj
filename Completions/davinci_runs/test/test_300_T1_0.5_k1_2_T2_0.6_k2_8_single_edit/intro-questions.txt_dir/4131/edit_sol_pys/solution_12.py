import sys


input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

pos = [0] * (n + 1)

for i in range(n):
    pos[a[i]] = i

l, r = 0, n

while l < r:
    m = (l + r) // 2
    c = [0] * (n + 1)
    for i in range(1, n + 1):
        if pos[i] < m:
            c[i] = 1
    cc = [0] * (n + 1)
    for i in range(1, n + 1):
        if pos[i] < m:
            cc[i] = 1
        else:
            cc[i] = -1
    for i in range(1, n + 1):
        cc[i] += cc[i - 1]
    if max(cc) == 0:
        l = m + 1
    else:
        r = m

ans = [0] * (n + 1)

for i in range(1, n + 1):
    if pos[i] < l:
        ans[i] = 1

print(l)
print(*ans[1:])
