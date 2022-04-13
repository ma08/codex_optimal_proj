#!/usr/bin/env python3

import sys

def main():
    K = int(sys.stdin.readline())
    if K == 1:
        print("0 1")
    else:
        A = [0, 1]
        B = [1, 1]
        for i in range(2, K+1):
            A.append(B[i-1])
            B.append(A[i-1] + B[i-1])
        print(str(A[K]) + " " + str(B[K]) + "\n")

if __name__ == '__main__':
    main()
