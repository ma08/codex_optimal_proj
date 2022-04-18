
import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if i < N-1:
            if A[i] == A[i+1]-1:
                count += C[A[i]-1]
        if i == N-1:
            count += C[A[i]-1]
    print(count)




if __name__ == '__main__':
    main()
