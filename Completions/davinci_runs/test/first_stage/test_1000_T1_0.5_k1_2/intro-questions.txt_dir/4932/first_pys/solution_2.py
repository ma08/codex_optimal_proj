
import sys
import math

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())
    if A + B > C + D:
        A, B, C, D = C, D, A, B
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
    
main()