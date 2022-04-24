

# for each possible number of people,
# determine whether it is possible to have
# exactly that many people

def solve(a):
	n = len(a)
	b = [0]
	for i in range(n):
		b.append(b[i] + a[i])
		b.append(b[i] - a[i])
	b.sort()
	c = [0]
	for i in range(1, len(b)):
		if b[i] != b[i-1]:
			c.append(b[i])
	m = len(c)
	# dp[i][j] = whether it's possible to have j people
	# and use people from the first i groups
	dp = [[False for j in range(m)] for i in range(n)]
	for i in range(n):
		dp[i][0] = True
	for i in range(n):
		for j in range(1, m):
			if i == 0:
				dp[i][j] = False
			else:
				dp[i][j] = dp[i][j-1] or (dp[i-1][j-1] and c[j] == c[j-1] + a[i])
	for j in range(m):
		if dp[n-1][j]:
			return j + 1
			
n = int(raw_input())
a = map(int, raw_input().split())
print solve(a)
