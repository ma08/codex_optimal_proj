

import sys
import math
from collections import deque

def main():
    n,d,k = [int(x) for x in input().split()]
    if k == 1:
        print("NO")
    elif k == 2:
        if d == 1:
            print("YES")
            for i in range(1,n):
                print(i+1,i)
        else:
            print("NO")
    elif k == 3:
        if d == 1:
            print("YES")
            for i in range(1,n):
                print(i+1,i)
        elif d == 2:
            print("YES")
            for i in range(1,n):
                print(i+1,i)
            print(3,1)
        else:
            print("NO")
    elif k == 4:
        if d == 1:
            print("YES")
            for i in range(1,n):
                print(i+1,i)
        elif d == 2:
            print("YES")
            for i in range(1,n):
                print(i+1,i)
            print(3,1)
        elif d == 3:
            print("YES")
            for i in range(1,n):
                print(i+1,i)
            print(2,1)
            print(3,2)
        else:
            print("NO")
    elif k == 5:
        if d == 1:
            print("YES")
            for i in range(1,n):
                print(i+1,i)
        elif d == 2:
            print("YES")
            for i in range(1,n):
                print(i+1,i)
            print(3,1)
        elif d == 3:
            print("YES")
            for i in range(1,n):
                print(i+1,i)
            print(2,1)
            print(3,2)
        elif d == 4:
            print("YES")
            for i in range(1,n):
                print(i+1,i)
            print(2,1)
            print(3,2)
            print(4,1)
        else:
            print("NO")
    else:
        if d == 1:
            print("YES")
            for i in range(1,n):
                print(i+1,i)
        elif d == 2:
            print("YES")
            for i in range(1,n):
                print(i+1,i)
            print(3,1)
        elif d == 3:
            print("YES")
            for i in range(1,n):
                print(i+1,i)
            print(2,1)
            print(3,2)
        elif d == 4:
            print("YES")
            for i in range(1,n):
                print(i+1,i)
            print(2,1)
            print(3,2)
            print(4,1)
        elif d == 5:
            print("YES")
            for i in range(1,n):
                print(i+1,i)
            print(2,1)
            print(3,2)
            print(4,1)
            print(5,1)
        else:
            print("NO")

if __name__ == "__main__":
    main()