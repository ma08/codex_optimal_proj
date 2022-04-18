

n, m = map(int, input().split())

arr = []
for i in range(n): arr.append(list(map(int, input().split())))

arr2 = [[0] * m for i in range(n)]
arr2[0][0] = arr[0][0]

for i in range(n):
    for j in range(m):
        if i > 0:
            arr2[i][j] = max(arr2[i][j], arr2[i - 1][j] + arr[i][j])
        if j > 0:
            arr2[i][j] = max(arr2[i][j], arr2[i][j - 1] + arr[i][j])

print(arr2[n - 1][m - 1])
