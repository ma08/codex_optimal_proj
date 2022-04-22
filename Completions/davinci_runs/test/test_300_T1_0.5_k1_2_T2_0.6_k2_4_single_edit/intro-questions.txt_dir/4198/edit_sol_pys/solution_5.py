import math

A, B, X = list(map(int, input().split()))
fail = True
if A + B <= X:
    for i in range(10**9):
        if A*i + B*len(str(i)) <= X:
            print(i)
            fail = False
            break
if fail:
    print(0)
