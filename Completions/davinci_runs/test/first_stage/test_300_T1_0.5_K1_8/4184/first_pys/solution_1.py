

N = int(input())
W = list(map(int, input().split()))

total = sum(W)
ans = total
for i in range(N):
    total -= W[i]
    ans = min(ans, abs(total - (sum(W[:i+1]))))

print(ans)