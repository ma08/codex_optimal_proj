
# SOLUTION 1

m, n = map(int, input().split())
u, l, r, d = map(int, input().split())

for i in range(u):
    print("#." * n + "#" + "." * r)

for i in range(m):
    print("#" + input() + "#" + "." * r)

for i in range(d):

# SOLUTION 2

m, n = map(int, input().split())
u, l, r, d = map(int, input().split())

for i in range(u):
    print(("#." * n + "#" + "." * r).rstrip())

for i in range(m):
    print(("#" + input() + "#" + "." * r).rstrip())

for i in range(d):
    print(("#." * n + "#" + "." * r).rstrip())
    print("#." * n + "#" + "." * r)
