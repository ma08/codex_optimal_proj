

a,b,c = map(int,input().split())
k = int(input())

if k%2 == 1:
    print(a-b*2+c)
else:
    print(a+b+c)
