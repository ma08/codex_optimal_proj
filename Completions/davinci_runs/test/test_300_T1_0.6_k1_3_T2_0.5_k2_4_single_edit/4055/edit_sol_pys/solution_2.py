n = int(input())
a = list(map(int, input().split()))

dp = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if a[i]==a[j]==1 and a[i+1]==a[j+1]==1:
            dp[i][j]=1
print(dp)

for i in range(1,n-1):
    if a[i-1]==a[i+1]==1 and a[i]==0:
        print("no")
        exit()
print("yes")

# count = 0
# for i in range(1, n - 1):
#     if a[i - 1] == a[i + 1] == 1 and a[i] == 0:
#         count += 1
# print(count)


