
import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return [int(x) for x in sys.stdin.readline().split()]

def main():
    N = read_int()
    M = [0] * N
    for i in range(N):
        M[i] = read_ints()

    a = [0] * N
    for i in range(N):
        for j in range(i+1, N):
            a[i] |= M[i][j]
            a[j] |= M[i][j]

    print(" ".join([str(x) for x in a]))

if __name__ == "__main__":
    main()
