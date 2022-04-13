
N, M, X = map(int, input().split())
A = []
C = []
for i in range(N):
    a = list(map(int, input().split()))
    C.append(a[0])
    A.append(a[1:])

ans = float('inf')

for i in range(1 << N):
    cost = 0
    skills = [0] * M
    for j in range(N):
        if (i >> j) & 1:
            cost += C[j]
            for k in range(M):
                skills[k] += A[j][k]
    if all([s >= X for s in skills]):
        ans = min(ans, cost)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
