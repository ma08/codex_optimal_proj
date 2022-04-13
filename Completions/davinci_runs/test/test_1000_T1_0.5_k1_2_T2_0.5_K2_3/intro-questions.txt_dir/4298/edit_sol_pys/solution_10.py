
import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    C = list(map(int, sys.stdin.readline().split()))

    ans = 0
    for i in range(N):
        ans += A[i] * B[i]
    for j in range(M):
        ans += C[j] * B[j]

    sys.stdout.write(str(ans) + '\n')


if __name__ == "__main__":
    main()
