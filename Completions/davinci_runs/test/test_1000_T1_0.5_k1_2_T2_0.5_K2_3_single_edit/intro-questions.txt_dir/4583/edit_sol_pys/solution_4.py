import sys
sys.setrecursionlimit(10**6)

import math
from itertools import product

def main():
    #get inputs
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * N
    for i in range(Q):
        S[int(input()) - 1] += 1
    A = [A[i] - K * S[i] for i in range(N)]

    #print result
    for a in A:
        if a > 0:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
