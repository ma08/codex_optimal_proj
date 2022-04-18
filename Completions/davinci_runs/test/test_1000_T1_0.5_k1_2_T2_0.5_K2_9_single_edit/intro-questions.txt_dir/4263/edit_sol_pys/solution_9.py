
import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    A = [0] * N
    B = [0] * M
    for i in range(N):
        A[i] = int(sys.stdin.readline())
    for i in range(M):
        B[i] = int(sys.stdin.readline())

    for i in range(M):
        for j in range(N):
            if A[j] <= B[i]:
                A[j] = B[i]
                break
        if j == N - 1:
            print('no')
            return
    print('yes')

if __name__ == '__main__':
    main()
