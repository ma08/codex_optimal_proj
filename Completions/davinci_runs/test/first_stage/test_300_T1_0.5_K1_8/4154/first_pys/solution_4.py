

N, M = map(int, input().split())

l = [0] * (N + 1)
r = [0] * (N + 1)

for i in range(M):
    L, R = map(int, input().split())
    l[L] += 1
    r[R] += 1

cnt = 0
s = 0
for i in range(1, N + 1):
    s += l[i]
    if s == 0:
        cnt += 1
    s -= r[i]

print(cnt)