

n,m = map(int,input().split())
p = list(map(int,input().split()))
l = []

for i in range(n):
    if p[i] == m:
        l.append(i)

if len(l) == 0:
    print(0)
elif len(l) == 1:
    print(1)
else:
    print(l[-1]-l[0]+1)