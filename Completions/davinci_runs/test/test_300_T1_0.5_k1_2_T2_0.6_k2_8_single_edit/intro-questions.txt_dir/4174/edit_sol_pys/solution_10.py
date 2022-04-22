

n,x=map(int,input().split())
l=list(map(int,input().split()))

cnt=1
d=0
for i in range(n):
    d+=l[i]
    if d<=x:
        cnt+=1
    else:
        break
print(cnt)
