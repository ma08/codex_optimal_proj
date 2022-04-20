

n,k=map(int,input().split())
a=list(map(int,input().split()))

def check(a,k):
    a=sorted(a)
    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    a=sorted(d.items(),key=lambda x:x[1],reverse=True)
    if len(a)<=k:
        return True
    else:
        return False

if check(a,k):
    print("YES")
    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    a=sorted(d.items(),key=lambda x:x[1],reverse=True)
    color=1
    for i in a:
        for j in range(i[1]):
            print(color,end=" ")
        color+=1
else:
    print("NO")