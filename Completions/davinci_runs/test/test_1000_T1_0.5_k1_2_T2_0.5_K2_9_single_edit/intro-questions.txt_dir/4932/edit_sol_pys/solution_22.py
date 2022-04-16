import sys

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())
    if A + B > C + D:
        A, B, C, D = C, D, A, B
    if P % (A + B) <= A:
        print('both')
    elif P % (A + B) > A:
        print('one')
    if M % (A + B) <= A:
        print('both')
    elif M % (A + B) > A:
        print('one')
    if G % (A + B) <= A:
        print('both')
    elif G % (A + B) > A:
        print('one')
    
main()
