

# cook your dish here
n, k = map(int,input().split())

if n<=k:
    print("YES")
    for i in range(n):
        print(i+1,i+1)
else:
    if n%2==0:
        print("YES")
        for i in range(n):
            if i%2==0:
                print(i+1,i+2)
            else:
                print(i+2,i+1)
    else:
        if k%2==0:
            print("YES")
            for i in range(n):
                if i%2==0:
                    print(i+1,i+2)
                else:
                    print(i+2,i+1)
            print(k,k)
        else:
            print("NO")