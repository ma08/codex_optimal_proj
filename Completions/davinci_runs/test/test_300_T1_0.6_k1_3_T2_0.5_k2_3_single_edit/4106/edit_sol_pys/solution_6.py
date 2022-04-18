

import sys
from collections import defaultdict
from itertools import combinations
from heapq import *
from math import inf
def main():
	n, k, x = map(int, sys.stdin.readline().split())
	a = list(map(int, sys.stdin.readline().split()))
	if x < k:
		print(-1)
		return
	if k == 1:
		print(sum(a[:x]))
		return
	# dp[i][j] = max sum for first i pictures, with j pictures left to be reposted
	dp = [[-inf for j in range(x+1)] for i in range(n+1)]
	dp[0][0] = 0
	for i in range(1, n+1):
		for j in range(1, x+1):
			# include this picture
			if i >= k:
				dp[i][j] = max(dp[i][j], dp[i-1][j-1] + a[i-1])
			# exclude this picture
			dp[i][j] = max(dp[i][j], dp[i-1][j])
			# include this picture, and some before it
			if i >= k:
				for l in range(1, min(i, k)):
					dp[i][j] = max(dp[i][j], dp[i-l][j-1] + sum(a[i-l:i]))
			# include this picture, and some before it, and some after it
			if i >= k:
				for l in range(1, min(i, k)):
					for m in range(1, min(n-i+1, k)):
						dp[i][j] = max(dp[i][j], dp[i-l][j-1] + sum(a[i-l:i]) + sum(a[i:i+m]))
			# include this picture, and some after it
			if i < n:
				for m in range(1, min(n-i+1, k)):
					dp[i][j] = max(dp[i][j], dp[i][j-1] + sum(a[i:i+m]))
	print(dp[n][x])
main()


# def main():
# 	n, k, x = map(int, sys.stdin.readline().split())
# 	a = list(map(int, sys.stdin.readline().split()))
# 	# dp[i][j] = max sum for first i pictures, with j pictures left to be reposted
# 	dp = [[-inf for j in range(x+1)] for i in range(n+1)]
# 	dp[0][0] = 0
# 	for i in range(1, n+1):
# 		for j in range(1, x+1):
# 			# include this picture
# 			if i >= k:
# 				dp[i][j] = max(dp[i][j], dp[i-1][j-1] + a[i-1])
# 			# exclude this picture
# 			dp[i][j] = max(dp[i][j], dp[i-1][j])
# 			# include this picture, and some before it
# 			if i >= k:
# 				for l in range(1, min(i, k)):
# 					dp[i][j] = max(dp[i][j], dp[i-l][j-1] + sum(a[i-l:i]))
# 			# include this picture, and some before it, and some after it
# 			if i >= k:
# 				for l in range(1, min(i, k)):
# 					for m in range(1, min(n-i+1, k)):
# 						dp[i][j] = max(dp[i][j], dp[i-l][j-1] + sum(a[i-l:i]) + sum(a[i:i+m]))
# 			# include this picture, and some after it
# 			if i < n:
# 				for m in range(1, min(n-i+1, k)):
# 					dp[i][j] = max(dp[i][j], dp[i][j-1] + sum(a[i:i+m]))
# 	print(dp[n][x])
# main()
