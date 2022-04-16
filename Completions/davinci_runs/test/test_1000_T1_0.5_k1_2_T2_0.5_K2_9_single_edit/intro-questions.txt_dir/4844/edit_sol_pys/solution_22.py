
import sys

def main():
    N = int(input())
    M = [0] * N
    for i in range(N):
        M[i] = list(map(int, input().split()))

    a = [0] * N
    for i in range(N):
        for j in range(i+1, N):
            a[i] |= M[i][j]
            a[j] |= M[i][j]

    print(" ".join([str(x) for x in a]))

if __name__ == "__main__":
    main()
