

import sys

def cocktail(A,B,C,I,J,K): 
    if A/I < B/J and A/I <= C/K:
        return A/I, B-A/I*J, C-A/I*K, 0
    elif B/J < A/I and B/J <= C/K:
        return A-B/J*I, B/J, C-B/J*K, 0
    elif C/K < A/I and C/K < B/J:
        return A-C/K*I, B-C/K*J, C/K, 0
    else:
        return 0, 0, 0, 1

def main():
    A,B,C = map(float, sys.stdin.readline().split())
    I,J,K = map(float, sys.stdin.readline().split())
    print('%0.6f %0.6f %0.6f' % cocktail(A,B,C,I,J,K))

if __name__ == '__main__':
    main()
