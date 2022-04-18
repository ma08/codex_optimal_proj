
n,a,b = map(int,input().split())

if a > b:
    a,b = b,a

print(min(n,a))
