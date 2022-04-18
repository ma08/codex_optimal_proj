

n,a,b = map(int,input().split())

if a > b:
    a,b = b,a

if b == 0:
    print(0)
else:
    print(min(n,a))
