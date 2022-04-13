
#-----main-----
n,m=map(int,input().split())

l=list(map(int,input().split()))

s=sum(l)

#print(s)

ans=0

for i in range(m):
    if l[i]<s/(4*m):
        ans+=1

if ans<=m-ans:
    print("Yes")
else:
    print("No")
