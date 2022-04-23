
import sys

def main():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    C = list(map(int, sys.stdin.readline().split()))

    prev = A[0]
    cnt = 0
    for i in range(1, N):
        if A[i] == prev + 1:
            cnt += 1
        prev = A[i]

    print(cnt)

if __name__ == '__main__':
    main()
