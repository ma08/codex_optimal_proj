

# Implement the solution here
def solve(n, m, edges):
    return -1, -1

# Inputs
n, m = [int(x) for x in input().split()]
edges = []
for i in range(m):
    edges.append([int(x) for x in input().split()])

# Solve the problem
res, path = solve(n, m, edges)

# Output
print(res)
