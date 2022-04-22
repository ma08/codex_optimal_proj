

n,a,b = map(int,input().split())

if a > b:
    a,b = b,a

if a == 0:
    print(0)
else:
    if n <= a:
        print(n)
    else:
        print(min(n,a))
