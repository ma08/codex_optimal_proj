

N = int(input())
A = list(map(int, input().split()))

S1 = 0
S2 = sum(A)

ans = abs(S1 - S2)
for i in range(1, N):
    S1 += A[i-1]
    S2 -= A[i-1]
    ans = min(ans, abs(S1 - S2))

print(ans)
