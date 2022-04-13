

# Implement the solution here
def solve(n, m, a, b):
    return -1

# Inputs
n, m = [int(x) for x in input().split()]
a = []
b = []
for i in range(m):
    x, y = [int(x) for x in input().split()]
    a.append(x)
    b.append(y)

# Solve the problem
res = solve(n, m, a, b)

# Output
print(res)
