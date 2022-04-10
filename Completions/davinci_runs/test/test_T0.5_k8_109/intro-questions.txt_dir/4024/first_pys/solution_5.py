

n, k = map(int, input().split())
s = input()

# We will use dynamic programming to solve the problem.
# The idea is to find the minimum cost for each subsequence of the string.
# We will use a 2D array to store the minimum cost for each subsequence.
# The array will be filled with the following values:
# 0 if the subsequence is empty
# 1 if the subsequence is a single character
# -1 if the subsequence is not a subsequence of the original string
# The minimum cost for the subsequence if it is a subsequence of the original string
#
# The array will be filled in the following manner:
# 1. If the current subsequence is not a subsequence of the original string,
#    we will mark it as -1
# 2. If the current subsequence is a subsequence of the original string,
#    we will find the minimum cost of the subsequence by finding the minimum
#    cost of all the substrings of the current subsequence.
#
# Once the array is filled, we will find the minimum cost for the subsequence
# of length n. If the cost is k, we are done. Else, we will try to find the cost
# for subsequences of length n-1, n-2 and so on.
#
# The time complexity of the algorithm is O(n^3)

# We will use a 2D array to store the minimum cost for each subsequence.
# The array will be filled with the following values:
# 0 if the subsequence is empty
# 1 if the subsequence is a single character
# -1 if the subsequence is not a subsequence of the original string
# The minimum cost for the subsequence if it is a subsequence of the original string
cost = [[0 for i in range(n)] for j in range(n)]

# Fill the cost array
for i in range(n):
    for j in range(n):
        if i == j:
            # The subsequence is a single character
            cost[i][j] = 1
        elif i > j:
            # The subsequence is empty
            cost[i][j] = 0
        else:
            # Check if the subsequence is a subsequence of the original string
            is_subsequence = True
            for k in range(i, j+1):
                if s[k] not in s[i:j+1]:
                    is_subsequence = False
                    break
            if is_subsequence:
                # Find the minimum cost of the subsequence
                # by finding the minimum cost of all the substrings
                # of the current subsequence
                min_cost = float('inf')
                for k in range(i, j+1):
                    for l in range(k, j+1):
                        if cost[k][l] != -1:
                            min_cost = min(min_cost, cost[k][l])
                cost[i][j] = min_cost
            else:
                # The subsequence is not a subsequence of the original string
                cost[i][j] = -1

# Find the minimum cost for the subsequence of length n
min_cost = cost[0][n-1]

# Try to find the cost for subsequences of length n-1, n-2 and so on
for i in range(n-1, 0, -1):
    if cost[0][i-1] != -1:
        min_cost = min(min_cost, cost[0][i-1])

if min_cost == k:
    print(cost[0][n-1])
else:
    print(-1)