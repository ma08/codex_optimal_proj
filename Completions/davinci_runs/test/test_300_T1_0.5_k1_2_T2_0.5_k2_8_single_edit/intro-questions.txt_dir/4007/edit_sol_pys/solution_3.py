
n,k=map(int,input().split())
l=list(map(int,input().split()))
m=l[k:]+l[:k]
print(*m)
