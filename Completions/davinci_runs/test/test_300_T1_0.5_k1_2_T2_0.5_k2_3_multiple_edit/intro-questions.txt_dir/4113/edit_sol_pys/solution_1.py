
N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(2 ** N):
    s = 0
    for j in range(N):
        if (i >> j) & 1 == 1:
            s += A[j]
    if s % M == 0:
        ans += 1
print(ans)
