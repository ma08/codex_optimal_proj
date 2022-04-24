N = int(input())
A = list(map(int, input().split()))


ans = 0
for i in range(N):
    ans += A[i] - 1

S1 = 0
S2 = sum(W)

ans = abs(S1 - S2)
for i in range(1, N):
    S1 += W[i-1]
    S2 -= W[i-1]
    ans = min(ans, abs(S1 - S2))

print(ans)
