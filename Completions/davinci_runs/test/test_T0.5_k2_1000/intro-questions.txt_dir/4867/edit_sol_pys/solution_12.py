
m, n = map(int, input().split())
u, l, r, d = map(int, input().split())

print("#"*(l+r+n)+"."*(m+u+d), end="\n")
for _ in range(u):
    print("#"*(l+r+n)+"."*(m+u+d), end="\n")
for _ in range(m):
    print("#"*l+input()+"#"*r, end="\n")
for _ in range(d):
    print("#"*(l+r+n)+"."*(m+u+d), end="\n")
