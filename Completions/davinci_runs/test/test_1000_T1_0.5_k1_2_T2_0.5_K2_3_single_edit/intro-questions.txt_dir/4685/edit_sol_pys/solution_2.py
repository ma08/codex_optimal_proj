
a,b,c = map(int,input().split())
k = int(input())

if k % 2 == 1:
    print(a*2+b+c)
else:
    print(a+b+c)
