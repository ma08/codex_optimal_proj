import sys

def cocktail(A,B,C,I,J,K):
    if A/I < B/J and A/I < C/K and A/I > 0:
        return A/I, B-(A/I)*J, C-(A/I)*K
    elif B/J < A/I and B/J < C/K and B/J > 0:
        return A-(B/J)*I, B/J, C-(B/J)*K
    elif C/K < A/I and C/K < B/J and C/K > 0:
        return A-(C/K)*I, B-(C/K)*J, C/K
    else:
        return A-C/K*I, B-C/K*J, C/K

def main():
    A,B,C = map(float, sys.stdin.readline().split())
    I,J,K = map(float, sys.stdin.readline().split())
    print('%0.6f %0.6f %0.6f' % cocktail(A,B,C,I,J,K))

if __name__ == '__main__':
    main()
