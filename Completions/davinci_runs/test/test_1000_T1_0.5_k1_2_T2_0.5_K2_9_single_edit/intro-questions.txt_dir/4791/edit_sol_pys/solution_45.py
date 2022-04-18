

import sys
from math import sqrt

def main():
    s = [int(i) for i in sys.stdin.readline().strip().split()]
    s.sort()
    a = s[0]
    b = s[1] - a
    c = s[2] - a
    d = s[3] - a
    #print(s)
    if d > b+c:
        print(0)
        return
    if d == b+c:
        print(sqrt((b+c)*(b+c-d)*(c-b+d)*(d-b-c))/4)
        return
    if d > c:
        print(0)
        return
    if d == c:
        print(sqrt((c)*(c-d)*(d-c)*(b+c-d))/4)
        return
    if d > b:
        print(0)
        return
    if d == b:
        print(sqrt((b)*(b-d)*(d-b)*(c+b-d))/4)
        return
    if d > 0:
        print(0)
        return
    if d == 0:
        print(sqrt((b)*(c)*(d)*(b+c+d))/4)
        return
    else:
        print("Error")

main()
