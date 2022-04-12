import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    A.sort()
    print(A[N-1] - A[0])

if __name__ == '__main__':
    main()
