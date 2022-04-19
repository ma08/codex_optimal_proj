'''
Task: 
Given a matrix of size n x m, you have to find the maximum sum of k x k sub-matrix.

Input:
First line contains two integers n and m, denoting the number of rows and columns in matrix. Next n lines contain m space separated integers. Next line contains an integer k.

Output:
Print the maximum sum of k x k sub-matrix.

Constraints:
1 <= n, m <= 100
1 <= k <= n, m
-1000 <= a[i][j] <= 1000

Sample input:
3 3
1 2 3
4 5 6
7 8 9
2

Sample output:
23

Explanation:
The maximum sum of 2 x 2 sub-matrix is 23.
'''


n,m,k = map(int, input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

def max_sum(matrix,n,m,k):
    dp = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[i][j] = matrix[i][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + matrix[i][j]
    return dp[n-1][m-k-1]

print(max_sum(matrix,n,m,k))
