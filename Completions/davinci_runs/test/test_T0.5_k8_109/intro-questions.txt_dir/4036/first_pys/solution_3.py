

n,k = [int(x) for x in input().split()]

if n<k:
    print("NO")
elif n==k:
    print("YES")
    print(*[1 for _ in range(k)])
else:
    print("YES")
    for i in range(k):
        if i==k-1:
            print(n,end=" ")
            break
        if i==0:
            print(1,end=" ")
            n-=1
        else:
            print(min(2*(i+1),n),end=" ")
            n-=min(2*(i+1),n)