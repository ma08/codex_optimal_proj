

n=int(input())
x=list(map(int,input().split()))
x=sorted(x)
ans=0
if x[0]!=x[-1]:
    ans+=1
    for i in range(1,n):
        if x[i]==x[i-1]:
            ans+=1
print(ans)