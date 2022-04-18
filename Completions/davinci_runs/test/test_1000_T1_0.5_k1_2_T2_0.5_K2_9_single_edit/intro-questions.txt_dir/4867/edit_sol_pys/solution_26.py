n, m = map(int, input().split())
u, l, r, d = map(int, input().split())


for i in range(u):
    print("#"*(l+r+n)+"."*(l+r))
for i in range(m):
    print("#"*l+input()+"#"*r)
for i in range(d):
    print("#"*(l+r+n)+"."*(l+r))
