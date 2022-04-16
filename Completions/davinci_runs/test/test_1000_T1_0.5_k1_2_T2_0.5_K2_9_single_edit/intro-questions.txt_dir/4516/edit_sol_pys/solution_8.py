

n, m = map(int, input().split())
x = list(map(int, input().split()))

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

# Calculate the final answer
ans = [0] * n
for i in range(n-1):
    ans[i] = sum(dist)
    dist[i] = dist[i] + abs(pos[i+2][0] - pos[i+1][0])
    if len(pos[i+2]) > 1:
        pos[i+2].pop(0)
ans[-1] = sum(dist)

print(*ans)
