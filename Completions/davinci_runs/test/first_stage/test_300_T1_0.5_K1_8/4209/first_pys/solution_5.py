

#Solution

n=int(input())
a=list(map(int,input().split()))
s=[]
for i in range(n):
    s.append(a[i])
    if i!=0:
        s[i]+=s[i-1]

c=0
m=[]
for i in range(n):
    for j in range(i,n):
        if i==0:
            if s[j]==0:
                c+=1
                m.append([j+1,j+1])
        else:
            if s[j]-s[i-1]==0:
                c+=1
                m.append([i+1,j+1])
print(c)
for i in m:
    print(i[0],i[1])