

# SOLUTION

m, n = map(int, input().split())  # m rows, n columns
u, l, r, d = map(int, input().split())  # u top, l left, r right, d bottom

for i in range(u):  # top
    print("#." * n + "#" + "." * r)  # print top

for i in range(m):  # middle
    print("#" + input() + "#" + "." * r)  # print middle

for i in range(d):  # bottom
    print("#." * n + "#" + "." * r)  # print bottom
