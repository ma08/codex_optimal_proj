
n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(1,n-1):
    if a[i]==0:
        if a[i-1]==1 and a[i+1]==1:
            ans+=1
            a[i+1]=0
print(ans)
