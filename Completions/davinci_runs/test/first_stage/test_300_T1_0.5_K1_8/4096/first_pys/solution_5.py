

n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
a.reverse()
ans=0
i=0
while m>0:
    m-=a[i]
    i+=1
    ans+=1
    if m<0:
        ans=-1
        break
    if i==n:
        i=0
print(ans)