import sys

X, A, B = map(int, input().split())

if A+B <= X+1:
    print("delicious")
elif A+B <= X+2:
    print("safe")
else:
    print("dangerous")
