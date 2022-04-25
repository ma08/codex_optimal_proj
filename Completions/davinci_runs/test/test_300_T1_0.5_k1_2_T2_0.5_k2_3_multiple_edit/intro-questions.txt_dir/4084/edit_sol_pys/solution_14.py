
n,a,b = map(int,input().split())

if a > b:
    a,b = b,a

if a == 0 or n == 1:
    print(0)
else:
    print(min(n,a)-1)
