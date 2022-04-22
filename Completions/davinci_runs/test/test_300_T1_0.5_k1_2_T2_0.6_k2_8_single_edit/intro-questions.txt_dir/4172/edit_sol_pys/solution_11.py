
n,k=map(int,input().split())
a=list(map(int,input().split()))
if k==1:
    print(0)
elif k==2:
    print(abs(a[0]-a[n-1]))
else:print(a[n-1]-a[0])
