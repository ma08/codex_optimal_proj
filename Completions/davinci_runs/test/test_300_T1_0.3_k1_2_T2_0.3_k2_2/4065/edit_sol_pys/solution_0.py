

n = int(input()) # number of problems
a = list(map(int, input().split())) # time to solve each problem

# dp[i] = max number of problems in a valid contest ending at problem i
dp = [1] * n
# for each problem

    # for each problem before it
for i in range(n):
        # if the time to solve problem i is less than half the time to solve problem j
    for j in range(i):
        if a[j] * 2 >= a[i]:
        # update dp[i] if needed
            break
        dp[i] = max(dp[i], dp[j] + 1)
# print the answer

print(max(dp))
