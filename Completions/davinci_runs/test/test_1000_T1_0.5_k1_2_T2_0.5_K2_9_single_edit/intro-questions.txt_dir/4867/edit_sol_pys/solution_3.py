

m, n = map(int, input().split())
u, l, r, d = map(int, input().split())

print("#"*(l+r+n)+"."*(n+l+r))
for _ in range(u):
    print("#"*(l+r+n)+"."*(n+l+r))
for _ in range(m):
    print("#"*l+input()+"#"*r)
for _ in range(d):
    print("#"*(l+r+n)+"."*(n+l+r))
