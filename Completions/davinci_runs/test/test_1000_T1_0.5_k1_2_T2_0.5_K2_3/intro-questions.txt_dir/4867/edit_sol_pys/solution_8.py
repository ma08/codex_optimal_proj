

#SOLUTION 

m, n = map(int, input().split())
u, l, r, d = map(int, input().split())

for i in range(u):
    print("#." * (n + 1) + "." * r)

for i in range(m):
    print("#" + input() + "#" + "." * r, end="")

for i in range(d):
    print("#." * (n + 1) + "." * r)
