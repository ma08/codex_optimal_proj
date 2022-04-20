
N = int(input())
W = list(map(int, input().split()))

ans = float('inf')
S = sum(W)

for i in range(1, N):
    S -= W[i - 1]
    ans = min(ans, abs(sum(W[:i]) - S))

print(ans)
