

n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

dp = [0]*h
dp[0] = 1 if l <= a[0] <= r else 0
for i in range(1, n):
    temp = [0]*h
    for j in range(h):
        if j >= a[i]:
            temp[j] = max(temp[j], dp[j-a[i]])
        if j >= a[i]-1:
            temp[j] = max(temp[j], dp[j-a[i]+1])
    dp = temp
print(max(dp))