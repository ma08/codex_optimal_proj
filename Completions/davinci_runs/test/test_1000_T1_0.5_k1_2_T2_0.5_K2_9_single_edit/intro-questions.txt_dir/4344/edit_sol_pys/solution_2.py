

n,k=map(int,input().split())
b=list(map(int,input().split()))
b.sort()
if len(set(b))<k:
    print("NO")
else:
    print("YES")
    for i in range(len(b)):
        if k==0:
            break
        if i==0:
            print(b[i],end=" ")
            k-=1
        elif b[i]!=b[i-1]:
            print(b[i],end=" ")
            k-=1
