

n,k=map(int,input().split())

if k==1:
    if n==1:
        print("YES")
        print("1")
    else:
        print("NO")
else:
    if n%2==0:
        print("YES")
        print(*[i+1 for i in range(k)])
    else:
        if k==2:
            print("NO")
        else:
            print("YES")
            print("2 1 ",*[i+2 for i in range(k-2)])