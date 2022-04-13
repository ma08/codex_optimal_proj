

#Program

n,p,q=map(int,input().split())

if(p//n==q//n):
    if(p%n==0):
        print("opponent")
    else:
        print("paul")
else:
    if(p//n>q//n):
        print("opponent")
    else:
        print("paul")