n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]+b[j]==k:
            c.append(a[i])
            c.append(b[j])
            break
        else:
            continue
if len(c)==0:
    print("empty")
else:
    for i in range(0,len(c),2):
        print(c[i],c[i+1])
