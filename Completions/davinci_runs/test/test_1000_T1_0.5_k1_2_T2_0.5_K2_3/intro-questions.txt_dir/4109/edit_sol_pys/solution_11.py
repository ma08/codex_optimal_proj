

N, M = map(int, input().split())
ans = 0
for i in range(N):
    A = list(map(int, input().split()))
    min_A = min(A)
    ans = max(ans, min_A)
print(ans)
