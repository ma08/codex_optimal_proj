

# input
X,A,B = map(int,input().split())

# output
if A >= X:
    print("delicious")
elif A < X and B < (X - A):
    print("dangerous")
else:
    print("safe")
