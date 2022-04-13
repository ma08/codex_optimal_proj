

#-----Solution-----

n, m = map(int, input().split()) # n = number of elements, m = number of queries
x = list(map(int, input().split())) # x = elements

# Save the positions of the elements in x in a dictionary
pos = {i:[] for i in range(1, n+1)}
for i in range(m):
    pos[x[i]].append(i+1)

# Calculate the distances between adjacent elements in x
dist = []
for i in range(m-1):
    dist.append(abs(pos[x[i]][0] - pos[x[i+1]][0]))
    if len(pos[x[i]]) > 1:
        pos[x[i]].pop(0)

# Calculate the final answers
ans = [0] * n
for i in range(n):
    ans[i] = sum(dist)
    if i < n-1:
        dist[i] = dist[i] + abs(pos[i+2][0] - pos[i+1][0])
        if len(pos[i+2]) > 1:
            pos[i+2].pop(0)

print(*ans)
