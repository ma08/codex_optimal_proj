

# Implement the solution here
def solve(n, m, a, b, c):
    return 0

# Inputs
n, m = [int(x) for x in input().split()]
a = []
c = []
b = []
for i in range(m):
    x, y, z = [int(x) for x in input().split()]
    a.append(x)
    c.append(z)
    b.append(y)

# Solve the problem
res = solve(n, m, a, b, c)

# Output
print(res)
