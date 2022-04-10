

a,b = map(int,input().split())
if a > b:
    a,b = b,a

if a == 1:
    print(2*(a+b))
else:
    print(2*(a+b-1))