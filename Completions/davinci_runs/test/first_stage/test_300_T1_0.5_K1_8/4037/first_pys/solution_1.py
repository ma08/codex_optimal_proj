

# SOLUTION
n,r = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
a = sorted(a,key = lambda x:x[1])
for i in range(n):
    r+=a[i][1]
    if r<0:
        print(i)
        break
else:
    print(n)