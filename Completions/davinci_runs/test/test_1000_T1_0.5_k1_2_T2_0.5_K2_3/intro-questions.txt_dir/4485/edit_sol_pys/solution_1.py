

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans += A[i] * (i+1) * (N-i) % (10**9+7)

print(ans)
