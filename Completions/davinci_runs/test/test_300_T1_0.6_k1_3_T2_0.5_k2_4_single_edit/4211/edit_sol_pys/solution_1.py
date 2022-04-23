

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

cnt = [-1] * N
cnt[0] = A[0]

for i in range(1, N):
    if cnt[i-1] < A[i]:
        cnt[i] = A[i]

cnt = [x for x in cnt if x != -1]

ans = 0

for i in range(M):
    ans += cnt[i]

print(ans)
