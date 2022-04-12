

import sys

X,A,B = map(int,input().split())

if A+B <= X: 
    print("delicious")
elif A+B <= X+1:
    print("safe")
else:
    print("dangerous")
