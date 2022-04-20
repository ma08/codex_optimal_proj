
import sys


def main():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    B = [0] * N
    for i in range(N):
        for j in range(A[i]):
            B[i] += (j + 1) * (A[i] - j)
    print(sum(B))


if __name__ == '__main__':
    main()
