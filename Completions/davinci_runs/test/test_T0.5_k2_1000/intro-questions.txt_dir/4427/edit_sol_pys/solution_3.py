

# Solved

# input
r, d, x2000 = map(int, input().split())

# output
for i in range(10):
    x2000 = r * x2000 - d
    print(x2000)
