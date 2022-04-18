

# input
X,A,B = map(int,input().split())

# output
if A <= X:
    print("delicious") 
elif A > X and B <= (A - X):
    print("dangerous")
else:
    print("safe")
