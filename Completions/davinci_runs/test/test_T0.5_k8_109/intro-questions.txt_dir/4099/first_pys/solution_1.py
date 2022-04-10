

import sys

def main():
    N,K,M = [int(i) for i in sys.stdin.readline().rstrip().split()]
    A = [int(i) for i in sys.stdin.readline().rstrip().split()]
    sum_A = sum(A)
    if sum_A >= M*N:
        print(-1)
    else:
        print(max(M*N-sum_A, 0))

if __name__ == "__main__":
    main()