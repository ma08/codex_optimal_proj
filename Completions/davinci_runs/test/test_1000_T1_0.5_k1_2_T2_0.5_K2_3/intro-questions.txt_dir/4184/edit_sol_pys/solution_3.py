
N = int(input())
W = list(map(int, input().split()))
ans = 100 * N
for i in range(1, N):
    ans = min(ans, abs(sum(W[:i]) - sum(W[i:])))
print(ans)
