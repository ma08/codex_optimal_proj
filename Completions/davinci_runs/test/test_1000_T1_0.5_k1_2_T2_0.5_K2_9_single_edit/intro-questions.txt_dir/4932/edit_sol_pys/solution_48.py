
import sys
import math

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())
    if A + B > C + D: A, B, C, D = C, D, A, B
    a, b, c = P % (A + B), M % (A + B), G % (A + B)
    print('one' if a > A else 'both')
    print('one' if b > A else 'both')
    print('one' if c > A else 'both')
    
main()
