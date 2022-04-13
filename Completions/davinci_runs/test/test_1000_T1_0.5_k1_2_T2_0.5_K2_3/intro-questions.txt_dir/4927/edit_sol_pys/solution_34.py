

#Program to check who will win the game

n,p,q=map(int,input().split())

if(p//n==q//n): #// is integer division
    if(p%n==0):
        print("opponent")
    else:
        print("paul")
else:
    if(p//n>q//n):
        print("opponent")
    else:
        print("paul")
