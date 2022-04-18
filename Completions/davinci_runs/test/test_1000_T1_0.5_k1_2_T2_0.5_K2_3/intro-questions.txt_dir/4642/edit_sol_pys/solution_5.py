

t = int(input())
for i in range(t):
    n,x,y = map(int,input().split())
    if 2*x != y:
        print(x,y,end=" ")
        for j in range(3,n+1):
            print(x+y,end=" ")
    else:
        print(x,y,end=" ")
        for j in range(3,n+1):
            print(x+((j-2)*(y-x)//(n-2)),end=" ")
    print()
