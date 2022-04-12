

n,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
count=0
for i in range(n):
    for j in range(i+1,n):
        if a[i]+a[j]>x:
            count=max(count,i+1)
            break
print(count)
