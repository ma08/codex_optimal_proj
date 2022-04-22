

N, X = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()

ans = 0
for i in range(N):
    ans += nums[i] * X
    if X > 1:
        X = X - 1

print(ans)
