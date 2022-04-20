
#----Solution-----
n = int(input())
a = list(map(int, input().split()))
if a[0]==1 or a[n-1]==1:
    print(-1)
else:
    res = n
    for i in range(1, n-1):
        if a[i]==0 and a[i-1]==1 and a[i+1]==1:
            res-=1
    print(res)