n,k,m = map(int,input().split())
a = list(map(int,input().split()))

score = sum(a)

if score + k < m*n:
    print(-1)
else:
    print(max(0,m*n-score))
