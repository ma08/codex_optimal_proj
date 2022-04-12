import sys

m, n = map(int, input().split())
u, l, r, d = map(int, input().split())

print("#"*(l+r+n)+"."*(m+u+d))
for _ in range(u):
    print("#"*(l+r+n)+"."*(m+u+d))
for _ in range(m):
    print("#"*l+sys.stdin.readline()+"#"*r)
for _ in range(d):
    print("#"*(l+r+n)+"."*(m+u+d))
