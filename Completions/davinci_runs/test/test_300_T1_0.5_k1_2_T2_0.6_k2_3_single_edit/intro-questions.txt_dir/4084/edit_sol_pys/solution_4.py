

n,a,b = map(int,input().split())

if a > b:
    a,b = b,a

if a == 0:
elif b == 0:
    print(min(n,a))
    print(0)
else:
    print(min(n,a))
