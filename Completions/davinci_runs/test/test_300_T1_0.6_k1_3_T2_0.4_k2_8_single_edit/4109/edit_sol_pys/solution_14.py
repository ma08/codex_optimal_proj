
import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    B = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    for i in range(N):
        for j in range(M):
            print(A[i][j] + B[j][i], end=" ")
        print()

if __name__ == "__main__":
    main()
