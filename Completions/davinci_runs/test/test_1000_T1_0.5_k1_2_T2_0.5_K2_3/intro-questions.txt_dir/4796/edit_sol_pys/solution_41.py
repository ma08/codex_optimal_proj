import sys

def cocktail(A,B,C,I,J,K):
    if A/I <= B/J and A/I <= C/K:
        return A/I, B-A/I*J, C-A/I*K, 1
    elif B/J <= A/I and B/J <= C/K:
        return A-B/J*I, B/J, C-B/J*K, 2
    else:
        return A-C/K*I, B-C/K*J, C/K, 3

def main():
    A,B,C = map(float, sys.stdin.readline().split())
    I,J,K = map(float, sys.stdin.readline().split())
    a,b,c,d = cocktail(A,B,C,I,J,K)
    print('%0.6f %0.6f %0.6f' % (a,b,c))
    print(d)

if __name__ == '__main__':
    main()
