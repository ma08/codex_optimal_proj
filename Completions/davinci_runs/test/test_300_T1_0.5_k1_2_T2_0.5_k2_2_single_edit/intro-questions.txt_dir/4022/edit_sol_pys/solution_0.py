
n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if a[i]+a[j]==a[k]:
                print(a[i],a[j],a[k])
