

#SOLUTION 1

m, n = map(int, input().split())
u, l, r, d = map(int, input().split())

for i in range(u):
    print("#." * n + "#" + "." * r, end = "\n")

for i in range(m):
    print("#" + input() + "#" + "." * r, end = "\n")

for i in range(d):
    print("#." * n + "#" + "." * r, end = "\n")
