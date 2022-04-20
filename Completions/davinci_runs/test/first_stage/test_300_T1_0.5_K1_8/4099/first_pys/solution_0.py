
#-----main-----
n,k,m = map(int,input().split())
a = list(map(int,input().split()))

max_score = sum(a) + k
min_score = sum(a) + 1

if max_score < m*n:
    print(-1)
else:
    print(m*n-sum(a))