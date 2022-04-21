

#Solution
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    x,y=n//2,n%2
    cost=x*min(a*2,b)+y*a
    print(cost)
