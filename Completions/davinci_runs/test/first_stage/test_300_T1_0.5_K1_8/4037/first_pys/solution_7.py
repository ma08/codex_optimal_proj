

n, r = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))

a.sort(key=lambda x:x[0])

dp = [0 for i in range(n)]

for i in range(n):
    if r < a[i][0]:
        break
    r = r + a[i][1]
    if r < 0:
        break
    dp[i] = 1

for i in range(1,n):
    dp[i] = dp[i] + dp[i-1]

print(max(dp))