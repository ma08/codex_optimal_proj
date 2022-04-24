
# Solution
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    if a*2<=b:
        print(n*a)
    else:
        if n%2==0:
            print(n*a//2)
        else:
            print((n//2+1)*a)
