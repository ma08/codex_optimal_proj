
#
# Solution

# cook your dish here
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    if n==1:
        print(a)
    elif n==2:
        print(min(2*a,b))
    else:
        print(min(2*a+b*((n-2)//2),b*((n+1)//2)))
