n = int(input())
nums = list(map(int, input().split()))
ans = 0

for i in range(n):
    for j in range(i + 1, n):
        ans += nums[i] * nums[j]

ans = ""
for i in range(n):
    if i < (k - 1) % n:
        ans += t[i]
    else:
        ans += t[(i + k) % n]

print(ans)
