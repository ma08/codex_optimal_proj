

n,k = map(int,input().split())

if n > 2*k or n < k or n % 2 == 1:
    print("NO")
    exit()

if n==k:
    print("YES")
    for i in range(1,n+1):
        print(i,end=" ")
        print(i)
    exit()

print("YES")

for i in range(1,n+1):
    if i%2 == 0:
        print(i,end=" ")
        print(i-1)
    else:
        print(i,end=" ")
        print(i+1)