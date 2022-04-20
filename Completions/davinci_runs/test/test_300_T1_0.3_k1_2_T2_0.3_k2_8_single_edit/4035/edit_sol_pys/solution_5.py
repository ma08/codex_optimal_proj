

import sys

def main():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    A.sort()
    print(A[0])

if __name__ == '__main__':
    main()
