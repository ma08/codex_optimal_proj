

import math
import sys

def main():
    # get input
    c = [list(map(int,input().split())) for i in range(3)]
    # check if there are possible sets of integers
    a = [c[i][0] - c[i][1] for i in range(3)]
    b = [c[i][1] - c[i][2] for i in range(3)]
    a.sort()
    b.sort()
    if a[0] == a[1] and a[1] == a[2] and b[0] == b[1] and b[1] == b[2]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
