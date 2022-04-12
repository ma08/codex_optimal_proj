

# Python3 program to find the smallest good number greater than or equal to n.

def good(n):

	# If n is already a good number
	if (n == 1):
		return n

	# Find all powers of 3 and store in a list
	powers = []
	i = 1
	while (3 ** i <= n):
		powers.append(3 ** i)
		i += 1

	# dp[i] stores the smallest good number greater than or equal to i.
	dp = [0 for i in range(n + 1)]

	# Initialize all dp values as n+1
	for i in range(1, n + 1):
		dp[i] = n + 1

	# Fill dp values starting from 2
	for i in range(2, n + 1):

		# For every power of 3, check if we can get a smaller good number by adding it
		for x in powers:

			# If i>x and dp[i-x] is a good number then we can make dp[i] a good number by adding x to it.
			if (i > x and dp[i - x] != n + 1):
				dp[i] = min(dp[i], dp[i - x] + x)

	# Return dp[n] if it is a good number else return -1
	return dp[n] if (dp[n] != n + 1) else -1

# Driver code
if __name__ == "__main__":

	n = int(input())
	print(good(n))
