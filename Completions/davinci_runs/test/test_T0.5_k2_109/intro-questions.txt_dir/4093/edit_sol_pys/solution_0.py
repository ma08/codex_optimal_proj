
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    if m==0 or n==1:
        print(0)
    elif m<n:
        print(m-1)
    else:
        print(m-n)
