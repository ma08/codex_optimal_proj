

n,a,b = map(int,input().split())

if a == 0:
    print(0)
    exit()

if a > b:
    a,b = b,a

print(min(n,a))
