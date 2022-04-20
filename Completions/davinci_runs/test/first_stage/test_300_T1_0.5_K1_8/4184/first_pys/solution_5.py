

n = int(input())
weights = list(map(int, input().split()))

if n == 2:
    print(abs(weights[0] - weights[1]))
    exit()

# 前半分と後半分の和の差分を全探索
ans = 100 * 100
for i in range(1, n):
    ans = min(ans, abs(sum(weights[:i]) - sum(weights[i:])))

print(ans)