#https://www.codechef.com/problems/CHN15A

t = int(input())
for i in range(t):
    n,x,y = map(int,input().split())
    if 2*x==y:
        print(x,y,end=" ")
        for j in range(3,n+1):
            print(x+y,end=" ")
    else:
        print(x,y,end=" ")
        l = [x,y]
        d = (y-x)//(n-2)
        for j in range(n-2):
            l.append(l[-1]+d)
        for j in l:
            print(j,end=" ")
    print()
