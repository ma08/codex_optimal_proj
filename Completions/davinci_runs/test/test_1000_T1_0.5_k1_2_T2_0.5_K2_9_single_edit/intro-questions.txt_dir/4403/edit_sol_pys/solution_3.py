

N, K = map(int, input().split())

A = list(map(int, input().split()))

ans = 0

for i in range(N):
    for j in range(i+1, N):
        if A[i] > A[j]:
            ans += 1

print(ans * K % (10**9 + 7))
