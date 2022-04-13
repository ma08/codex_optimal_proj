
import sys

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        print(A[i], end=' ')
        if A[i] % 2 == 0:
            print(A[i] // 2)
        else:
            print(A[i] * 2)

if __name__ == '__main__':
    main()
