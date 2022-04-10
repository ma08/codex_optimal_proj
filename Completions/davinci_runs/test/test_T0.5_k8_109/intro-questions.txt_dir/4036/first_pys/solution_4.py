

n,k = map(int,input().split())

if k==1:
    print("YES")
    print(n)
elif n<k:
    print("NO")
elif n==k:
    print("YES")
    print(" ".join([str(1) for i in range(k)]))
else:
    l=[1]
    for i in range(1,k):
        l.append(2*l[i-1])
        if sum(l)>n:
            print("NO")
            break
    else:
        print("YES")
        print(" ".join([str(i) for i in l]))