import sys


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        for j in range(A[i]):
            B[i] += (j + 1) * (A[i] - j)
    print(sum(B))


def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        for j in range(A[i]):
            B[i] += (j + 1) * (A[i] - j)
    print(sum(B))


if __name__ == '__main__':
    main()
