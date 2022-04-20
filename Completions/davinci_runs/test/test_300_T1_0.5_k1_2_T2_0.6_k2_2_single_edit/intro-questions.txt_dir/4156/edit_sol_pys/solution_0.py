import math
n,w=map(int,input().split())
a=list(map(int,input().split()))
if sum(a)<=w:
    print(w-sum(a))
elif sum(a)>w:
    print(math.ceil(sum(a)-w))
