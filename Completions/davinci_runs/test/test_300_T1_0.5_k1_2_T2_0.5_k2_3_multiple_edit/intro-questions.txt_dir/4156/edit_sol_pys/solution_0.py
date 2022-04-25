
n,w=map(int,input().split())
a=list(map(int,input().split()))
print(max(w-abs(sum(a)),0))
