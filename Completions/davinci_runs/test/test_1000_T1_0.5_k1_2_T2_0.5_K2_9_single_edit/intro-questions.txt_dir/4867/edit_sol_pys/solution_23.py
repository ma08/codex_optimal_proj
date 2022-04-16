

#SOLUTION

m, n = map(int, input().split())
u, l, r, d = map(int, input().split())

for i in range(u):
    print("#." * n + "#" + "." * r)

for i in range(m - (u + d)):
    print("#" + input() + "#" + "." * r)

for i in range(d):
    print("#." * n + "#" + "." * r)
