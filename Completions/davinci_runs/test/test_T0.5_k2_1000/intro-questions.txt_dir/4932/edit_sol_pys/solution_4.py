
import sys
import math

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())
    if A + C > B + D:
        A, B, C, D = B, A, D, C
    a = P % (A + B)
    b = M % (A + B)
    c = G % (A + B)
    if a <= A and b <= A and c <= A:
        print('both', 'both', 'both')
    elif a > A and b > A and c > A:
        print('one', 'one', 'one')
    elif a <= A and b <= A and c > A:
        print('both', 'both', 'one')
    elif a <= A and b > A and c <= A:
        print('both', 'one', 'both')
    elif a > A and b <= A and c <= A:
        print('one', 'both', 'both')
    elif a <= A and b > A and c > A:
        print('both', 'one', 'one')
    elif a > A and b <= A and c > A:
        print('one', 'both', 'one')
    elif a > A and b > A and c <= A:
        print('one', 'one', 'both')
    
main()
