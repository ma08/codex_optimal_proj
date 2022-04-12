

import sys,math
N = int(input())

for i in range(N):
    x,y = map(int,input().split())
    if x == y:
        if x % 2 == 0:
            print(x*2)
        else:
            print(x*2-1)
    elif x == y+2:
        if x % 2 == 0:
            print(x+y)
        else:
            print(x+y-1)
    else:
        print("No Number")
