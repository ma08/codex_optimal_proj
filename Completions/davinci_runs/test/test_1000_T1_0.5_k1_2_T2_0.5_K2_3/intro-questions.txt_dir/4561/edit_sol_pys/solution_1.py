

# input
X,A,B = map(int,input().split())

# output
if A <= X:
    print("YES")
elif A > X and B <= (A - X):
    print("NO")
else:
    print("YES")
