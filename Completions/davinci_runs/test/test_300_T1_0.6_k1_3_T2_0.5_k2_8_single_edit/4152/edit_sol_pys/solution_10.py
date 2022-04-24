

n = int(input())
l = list(map(int,input().split()))

if n==1 and l[0]!=1:
    print(1)
elif n==1 and l[0]==1:
    print(0)
else:
    print(n-max(l))
