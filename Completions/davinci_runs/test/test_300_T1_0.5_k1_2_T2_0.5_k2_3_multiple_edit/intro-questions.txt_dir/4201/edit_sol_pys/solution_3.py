import sys
sys.setrecursionlimit(10**9)


def dfs(i, j, cnt):
	if cnt == K:
		return 1
	if i == H:
		return 0
	if j == W:
		return dfs(i + 1, 0, cnt)
	if A[i][j] == 1:
		return dfs(i, j + 1, cnt)

	A[i][j] = 1
	ans1 = dfs(i, j + 1, cnt + 1)
	A[i][j] = 0
	ans2 = dfs(i, j + 1, cnt)
	return ans1 + ans2

H, W, K = map(int, input().split()) 
A = [[0 for i in range(W)] for j in range(H)]
print(dfs(0, 0, 0))
