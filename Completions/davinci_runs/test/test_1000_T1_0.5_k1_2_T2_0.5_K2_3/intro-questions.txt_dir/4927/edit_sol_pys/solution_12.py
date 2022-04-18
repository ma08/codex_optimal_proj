
N = int(input())
A = [int(x) for x in input().split()]
if N % 2 == 1:
    if A[0] == 1:
        print("First")
    else:
        print("Second") 
elif N % 2 == 0:
    if A[0] == 1:
        print("Second")
    else:
        print("First")
