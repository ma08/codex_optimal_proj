

import sys, numpy as np

def main():
    N, M = map(int, sys.stdin.readline().strip().split())
    mat = np.array([list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)])
    print(mat)
    K = int(sys.stdin.readline().strip())
    for k in range(K):
        i, j = map(int, sys.stdin.readline().strip().split())
        mat[i-1][j-1] = 0
    print(mat)
    print(np.sum(mat))

if __name__ == "__main__":
    main()
