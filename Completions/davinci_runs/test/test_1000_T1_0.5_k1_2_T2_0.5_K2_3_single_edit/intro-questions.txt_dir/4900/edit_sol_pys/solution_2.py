import sys

# read input
n = int(sys.stdin.readline())
distances = []
for i in range(n):
    distances.append([int(x) for x in sys.stdin.readline().split()])

# calculate the minimum spanning tree
mst = []
visited = [False]*n
visited[0] = True
while False in visited:
    min_dist = float('inf')
    min_i = -1
    min_j = -1
    for i in range(n):
        if visited[i]:
            for j in range(n):
                if not visited[j] and distances[i][j] < min_dist:
                    min_dist = distances[i][j]
                    min_i = i
                    min_j = j
    mst.append((min_i+1, min_j+1))
    visited[min_j] = True

# print the minimum spanning tree
for road in mst:
    print(road[0], road[1])
