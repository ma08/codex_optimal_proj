

# cook your dish here
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    if n==1:
        print(0)
    else:
        print((m-n+1)*2)