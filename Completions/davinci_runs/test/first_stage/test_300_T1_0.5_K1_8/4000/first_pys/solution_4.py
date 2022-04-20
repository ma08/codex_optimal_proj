

# Solution:

n = int(input())
edges = []
for i in range(n-1):
    a, b = map(int, input().split())
    edges.append([a, b])

path = [[0] * n for i in range(n)]
for i in edges:
    path[i[0]-1][i[1]-1] = 1
    path[i[1]-1][i[0]-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            path[i][j] = path[i][j] or path[i][k] and path[k][j]

max_path = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and k != i:
                max_path = max(max_path, path[i][j] + path[j][k] + path[k][i])

print(max_path)
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and k != i:
                if path[i][j] + path[j][k] + path[k][i] == max_path:
                    print(i+1, j+1, k+1)
                    exit()