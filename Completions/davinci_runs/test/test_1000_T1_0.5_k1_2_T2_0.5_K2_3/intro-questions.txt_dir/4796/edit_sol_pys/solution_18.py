


import sys

def cocktail_shaker(A,B,C,I,J,K):
    if A/I < B/J and A/I < C/K:
        return A/I, B-A/I*J, C-A/I*K
    elif B/J < A/I and B/J < C/K:
        return A-B/J*I, B/J, C-B/J*K
    else:
        return A-C/K*I, B-C/K*J, C/K

def main():
    A,B,C = map(float, sys.stdin.readline().split())
    I,J,K = map(float, sys.stdin.readline().split())
    print('%0.6f %0.6f %0.6f' % cocktail_shaker(A,B,C,I,J,K))

if __name__ == '__main__':
    main()
