

import math
import sys

def main():
    # get input
    c = []
    for i in range(3):
        c.append(list(map(int,input().split())))
    # check if there are possible sets of integers 
    a = []
    b = []
    for i in range(3):
        a.append(c[i][0] - c[i][1])
        b.append(c[i][1] - c[i][2])
    a.sort()
    b.sort()
    if a[0] == a[1] == a[2] and b[0] == b[1] == b[2]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
