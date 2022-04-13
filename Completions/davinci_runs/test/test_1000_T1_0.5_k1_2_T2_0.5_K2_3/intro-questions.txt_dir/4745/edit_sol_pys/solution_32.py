
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    x=l[0]
    y=l[1]
    c=0
    for i in range(2,n):
        if x+y+l[i]<=sum(l):
            c+=1
            x=y
            y=l[i]
    print(c)
