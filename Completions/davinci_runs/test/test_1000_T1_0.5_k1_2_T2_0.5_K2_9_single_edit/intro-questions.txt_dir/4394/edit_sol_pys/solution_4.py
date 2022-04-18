

# Implement the solution
def solve(n, m, edges):
    return -1

# Inputs
n, m = [int(x) for x in input().split()]
edges = []
for i in range(m):
    u, v = [int(x) for x in input().split()]
    edges.append((u, v))

# Solve the problem
res = solve(n, m, edges)

# Output
print(res)
