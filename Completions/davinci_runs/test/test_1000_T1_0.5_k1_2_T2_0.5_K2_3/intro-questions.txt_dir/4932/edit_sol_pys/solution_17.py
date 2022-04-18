
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
    if a <= A or b <= A or c <= A:
        print('both', end = ' ')
    if a > A and b > A and c > A:
        print('one', end = ' ')
    
main()
