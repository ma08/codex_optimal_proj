n,k,m = map(int,input().split())
a = list(map(int,input().split()))

s = sum(a)

if m*n - s > k: 
    print(-1)
else:
    print(m*n - s)
