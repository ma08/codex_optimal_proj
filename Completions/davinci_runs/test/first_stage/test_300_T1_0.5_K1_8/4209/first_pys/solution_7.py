

n = int(input())
a = list(map(int,input().split()))

# dp[i][j] = max number of block from i to j
# dp[i][j] = dp[i+1][j] + 1 if all a[i] == a[i+1] == ... == a[j]
# dp[i][j] = max(dp[i+1][j], dp[i][j-1]) otherwise
# dp[i][j] = 1 if i == j

dp = [[0]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1
for i in range(n-1,-1,-1):
    for j in range(i+1,n):
        if a[i] == a[j]:
            if all(a[i] == a[k] for k in range(i,j+1)):
                dp[i][j] = dp[i+1][j] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i+1][j])

# print(dp)

# now we have the max number of blocks, we can find the blocks
# we can start from anywhere, and keep track of the sum of the block
# if we find a[k] == sum, we found a new block
# if we find a[k] != sum, we need to split the block
# we can do this by finding the largest block that has a[k] == sum,
# and the largest block that has a[k] != sum
# we can find these blocks by looking at the dp table
# we can also use these dp values to find the next block

ans = []
i = 0
while i < n:
    # print(i)
    if i == n-1:
        ans.append((i,i))
        break
    # find the largest block that has a[i] == sum
    j = i+1
    while j < n:
        if dp[i][j] == dp[i+1][j]:
            j += 1
        else:
            break
    # print(i,j)
    # find the largest block that has a[i] != sum
    k = i+1
    while k < n:
        if dp[i][k] == dp[i][k-1]:
            k += 1
        else:
            break
    # print(i,k)
    # print(i,j,k)
    # find the next block
    if j < n and k < n:
        if dp[i][j] > dp[i][k]:
            ans.append((i,j-1))
            i = j
        else:
            ans.append((i,k-1))
            i = k
    elif j < n:
        ans.append((i,j-1))
        i = j
    elif k < n:
        ans.append((i,k-1))
        i = k
    else:
        ans.append((i,n-1))
        i = n

print(len(ans))
for a,b in ans:
    print(a+1,b+1)