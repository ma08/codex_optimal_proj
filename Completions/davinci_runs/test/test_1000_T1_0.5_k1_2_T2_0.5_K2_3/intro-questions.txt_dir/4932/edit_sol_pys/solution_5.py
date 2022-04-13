import sys

def main():
    A, B, C, D = map(int, sys.stdin.readline().split())
    P, M, G = map(int, sys.stdin.readline().split())
    A, B, C, D = B, A, D, C
    if A + C > B + D:
        A, B, C, D = C, D, A, B
    a = P % (A + B)
    b = M % (A + B)
    c = G % (A + B)
    if a <= A:
        print('both')
    else:
        print('one')
    if b <= A:
        print('both')
    else:
        print('one')
    if c <= A:
        print('both')
    else:
        print('one')

main()
