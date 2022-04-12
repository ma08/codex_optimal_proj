
#test
import sys

A,B,C,D = map(int, sys.stdin.readline().split())

if A>C:
    print("Yes")
elif A<C:
    print("No")
else:
    if B>D:
        print("Yes")
    else:
        print("No")
