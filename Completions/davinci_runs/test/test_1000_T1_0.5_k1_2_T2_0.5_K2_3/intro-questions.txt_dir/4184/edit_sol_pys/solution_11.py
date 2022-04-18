

N = int(input())
W = list(map(int, input().split()))
sum_w = sum(W)
ans = float('inf')
T = 0
for i in range(N):
    T += W[i]
    ans = min(ans, abs(sum_w - 2 * T))
print(ans)
