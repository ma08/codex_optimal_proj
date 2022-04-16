
import sys
import math

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())
    if A + B <= C + D:
        a = P % (A + B)
        b = M % (A + B)
        c = G % (A + B)
        if a <= A:
            print('both')
        elif a > A:
            print('one')
        if b <= A:
            print('both')
        elif b > A:
            print('one')
        if c <= A:
            print('both')
        elif c > A:
            print('one')
    elif A + B > C + D:
        a = P % (C + D)
        b = M % (C + D)
        c = G % (C + D)
        if a <= C:
            print('both')
        elif a > C:
            print('one')
        if b <= C:
            print('both')
        elif b > C:
            print('one')
        if c <= C:
            print('both')
        elif c > C:
            print('one')
    
main()
