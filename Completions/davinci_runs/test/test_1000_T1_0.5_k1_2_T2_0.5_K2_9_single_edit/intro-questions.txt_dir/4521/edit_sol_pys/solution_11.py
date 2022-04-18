

# SOLUTION
def minimum_distance(x, v):
    n = len(x)
    x = [x[i] + v[i] for i in range(n)]
    x.sort()

x = [x[i] + v[i] for i in range(n)]

x.sort()

d = 0
for i in range(n - 1):
    d += x[i + 1] - x[i]

print(d)
