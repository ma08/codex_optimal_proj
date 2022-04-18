# B - 

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if A[i] + A[j] == K:
            ans += 1

print(ans)
