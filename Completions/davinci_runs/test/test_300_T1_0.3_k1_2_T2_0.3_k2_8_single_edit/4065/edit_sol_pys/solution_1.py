
n = int(input())
a = list(map(int, input().split()))

# dp[i] = max number of problems in a valid contest ending at a[i] (including a[i])
dp = [1] * n

for i in range(1, n):
    for j in range(i): # j < i
        if a[j] * 2 >= a[i]: # if a[j] is too big, we can't use it
            break # so we can stop checking for smaller j
        dp[i] = max(dp[i], dp[j] + 1) # otherwise, we can use a[j]

print(max(dp))
