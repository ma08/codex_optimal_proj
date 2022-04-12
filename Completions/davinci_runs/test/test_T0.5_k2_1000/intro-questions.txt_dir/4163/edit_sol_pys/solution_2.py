# -*- coding: utf-8 -*-

import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    T = [0] * N
    for i in range(N):
        T[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(N-2):
        if T[i][0] == T[i][1] and T[i+1][0] == T[i+1][1] and T[i+2][0] == T[i+2][1]:
            print("Yes")
            return
    print("No")
    return

if __name__ == "__main__":
    main()
