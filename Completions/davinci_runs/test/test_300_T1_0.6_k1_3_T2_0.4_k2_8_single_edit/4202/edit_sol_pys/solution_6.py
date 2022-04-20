
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = 0
for i in range(M):
    ans += A[i]
if ans > N:
    print(-1)
else:
    print(ans)
