
import sys
from math import sqrt

def main():
    s = [int(i) for i in sys.stdin.readline().strip().split()]
    s.sort()
    a = s[0]
    b = s[1]
    c = s[2]
    d = s[3]
    # print(s)
    if d > a+b+c:
        print(0)
        return
    if d == a+b+c:
        print(sqrt((a+b+c)*(a+b-c)*(a+c-b)*(b+c-a))/4.0)
        return
    if d > a+b:
        print(0)
        return
    if d == a+b:
        print(sqrt((a+b)*(a+b-c)*(a+b-d)*(c-a+b)*(d-a-b))/4.0)
        return
    if d > a+c:
        print(0)
        return
    if d == a+c:
        print(sqrt((a+c)*(a+c-b)*(a+c-d)*(b-a+c)*(d-a-c))/4.0)
        return
    if d > b+c:
        print(0)
        return
    if d == b+c:
        print(sqrt((b+c)*(b+c-a)*(b+c-d)*(a-b+c)*(d-b-c))/4)
        return
    if d > a:
        print(0)
        return
    if d == a:
        print(sqrt((a)*(a-b)*(a-c)*(a-d)*(b+c+d-a))/4)
        return
    if d > b:
        print(0)
        return
    if d == b:
        print(sqrt((b)*(b-a)*(b-c)*(b-d)*(a+c+d-b))/4)
        return
    if d > c:
        print(0)
        return
    if d == c:
        print(sqrt((c)*(c-a)*(c-b)*(c-d)*(a+b+d-c))/4)
        return
    if d > 0:
        print(0)
        return
    if d == 0:
        print(sqrt((a)*(b)*(c)*(d)*(a+b+c+d))/4)
        return
    else:
        print("Error")

main()
