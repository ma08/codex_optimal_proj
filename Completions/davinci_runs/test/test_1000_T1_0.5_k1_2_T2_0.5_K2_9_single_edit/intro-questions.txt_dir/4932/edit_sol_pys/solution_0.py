
import sys
import math

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())
    if A + B < C + D:
        A, B, C, D = C, D, A, B # A + B < C + D
    if P % (A + B) <= A:
        print('both') # P
    elif P % (A + B) > A:
        print('one') # P
    if M % (A + B) <= A:
        print('both') # M
    elif M % (A + B) > A:
        print('one') # M
    if G % (A + B) <= A:
        print('both') # G
    elif G % (A + B) > A:
        print('one') # G
    
main()
