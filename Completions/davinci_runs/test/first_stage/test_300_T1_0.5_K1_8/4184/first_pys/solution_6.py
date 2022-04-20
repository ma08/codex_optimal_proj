

# input
N = int(input())
W = list(map(int, input().split()))

# initialization
ans = float('inf')

# solve
for i in range(1, N):
    ans = min(ans, abs(sum(W[:i]) - sum(W[i:])))

# output
print(ans)