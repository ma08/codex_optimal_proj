
# cook your dish here.
# cook your dish here.

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[]
    for j in range(n):
        c.append(a[j]+b[j])
    print(*c)
