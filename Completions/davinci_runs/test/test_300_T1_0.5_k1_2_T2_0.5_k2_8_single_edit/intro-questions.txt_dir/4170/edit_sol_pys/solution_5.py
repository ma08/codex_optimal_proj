
N = int(input())
nums = list(map(int, input().split()))

ans = 0
cur = 0
for i in range(N-1):
    if nums[i+1] <= nums[i]:
        cur += 1
    else:
        ans = max(ans, cur)
        cur = 0
print(max(ans, cur))
