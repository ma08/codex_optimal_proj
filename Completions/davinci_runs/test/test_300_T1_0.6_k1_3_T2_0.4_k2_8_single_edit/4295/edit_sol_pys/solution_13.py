
import sys

def main():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    Q = int(sys.stdin.readline())
    BC = [list(map(int, sys.stdin.readline().split())) for _ in range(Q)]

    for i in range(Q):
        B, C = BC[i]
        for j in range(N):
            if A[j] == B:
                A[j] = C
        print(sum(A))


if __name__ == '__main__':
    main()
