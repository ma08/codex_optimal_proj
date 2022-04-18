

# SOLUTION

m, n = map(int, input().split())  # Get the input
u, l, r, d = map(int, input().split())  # Get the input

for i in range(u):  # Top
    print("#." * n + "#" + "." * r)

for i in range(m):  # Middle
    print("#" + input() + "#" + "." * r)

for i in range(d):  # Bottom
    print("#." * n + "#" + "." * r)
