
m, n = map(int, input().split())
u, l, r, d = map(int, input().split())

for _ in range(u):
    print("#." * n + "#" + "." * r)

for _ in range(m):
    print("#" + input() + "#" + "." * r)

for _ in range(d):
    print("#." * n + "#" + "." * r)
