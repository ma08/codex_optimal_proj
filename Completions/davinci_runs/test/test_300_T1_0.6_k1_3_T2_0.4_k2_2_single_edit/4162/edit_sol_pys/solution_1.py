
import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        for j in range(A[i]):
            B[i + 1] += (j + 1) * (A[i] - j)
    print(sum(B[1:]))


if __name__ == '__main__':
    main()
