
n,m=map(int,input().split())
k=[]
for i in range(n):k.append(input())
t=0
for i in range(m):
    if k[0][i]=='_':t+=1
print(t)
