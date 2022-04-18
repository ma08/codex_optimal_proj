

N, M = map(int, input().split())
L = [0] * N
R = [0] * N

for i in range(M):
    l, r = map(int, input().split())
    L[l-1] += 1
    R[r-1] += 1

ans = 0
tmp = 0
for i in range(N):
    tmp += L[i]
    if tmp == M:
        ans += 1
    tmp -= R[i]

print(ans)
