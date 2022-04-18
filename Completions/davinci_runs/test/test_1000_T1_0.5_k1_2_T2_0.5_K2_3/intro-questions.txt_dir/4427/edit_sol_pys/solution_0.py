

# Solved

# input
r, D, x2000 = map(int, input().split())

# output
for _ in range(10):
    x2000 = r * x2000 - D
    print(x2000)
