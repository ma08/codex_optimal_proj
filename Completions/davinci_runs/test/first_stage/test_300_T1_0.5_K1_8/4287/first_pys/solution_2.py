

#-------------------------------------------------------------------------------

"""
    Approach : 
        - Greedy
        - We need to move in the rain with at least one umbrella.
        - We can't move in the rain with two umbrella.
        - We can move in the rain with one umbrella.
        - We can move outside the rain without umbrella.
        - We can move outside the rain with umbrella.
        - We can't move in the rain without umbrella.
        - We can't move outside the rain with two umbrella.


    Complexity Analysis :
        - Time Complexity: O(N * M)
        - Space Complexity: O(N + M)
"""

#-------------------------------------------------------------------------------

# Python3 program to find minimum fatigue 
# to travel from 0 to a 

# Function to find minimum fatigue 
def findMinFatigue(a, n, m, l, r, x, p): 

	# dp[i][j] is the minimum fatigue 
	# to travel from 0 to i if we have 
	# j umbrellas with us 
	dp = [[float('inf') for i in range(m + 1)] 
			for j in range(a + 1)] 

	# Initialize dp[0][j] = 0 
	# It is already 0 

	# Initialize dp[i][1] 
	for i in range(a + 1): 
		if i not in l: 
			dp[i][1] = 0

	# Initialize dp[i][0] 
	# It is impossible to travel 
	# from 0 to i with 0 umbrellas 
	for i in range(1, a + 1): 
		dp[i][0] = float('inf') 

	# Calculate dp[i][j] 
	for i in range(1, a + 1): 
		for j in range(1, m + 1): 

			# If we can travel from 0 to i 
			# with j - 1 umbrellas 
			if dp[i][j - 1] != float('inf'): 
				dp[i][j] = min(dp[i][j], dp[i][j - 1]) 

			# If we can travel from 0 to i 
			# without umbrella 
			if i not in l: 
				dp[i][j] = min(dp[i][j], dp[i - 1][j]) 

			# If we can travel from 0 to i 
			# with j - 1 umbrella and we can 
			# travel from i - 1 to i with umbrella 
			if dp[i][j - 1] != float('inf') and i - 1 in l: 
				dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + p[x.index(i - 1)]) 

	# If we can't travel from 0 to a 
	if dp[a][m] == float('inf'): 
		return -1

	# Else return minimum fatigue 
	return dp[a][m] 

# Driver Code 
if __name__ == '__main__': 
	a, n, m = 10, 2, 4
	l = [3, 8] 
	r = [7, 10] 
	x = [0, 10, 3, 4, 8, 1, 1, 2] 
	p = [10, 5, 4, 1, 1, 2] 
	print(findMinFatigue(a, n, m, l, r, x, p)) 

# This code is contributed by AnkitRai01