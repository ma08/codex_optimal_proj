

# find the minimum number of people
# that must be removed to make the rest
# satisfied

def solve(n, a):
	# dp[i][j] = minimum number of people to be removed
	# to make the first i people happy, with j additional
	# people removed
	dp = [[0 for j in range(n + 1)] for i in range(n)]
	for i in range(n):
		for j in range(n + 1):
			dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
			if a[i] + j <= n:
				dp[i][j] = min(dp[i][j], dp[i][a[i] + j])
			if a[i] - j >= 0:
				dp[i][j] = min(dp[i][j], dp[i][j-a[i] + j])
	return dp[n-1][0]

test = int(raw_input())
for t in range(test):
	n = int(raw_input())
	a = map(int, raw_input().split())
	print solve(n, a)
