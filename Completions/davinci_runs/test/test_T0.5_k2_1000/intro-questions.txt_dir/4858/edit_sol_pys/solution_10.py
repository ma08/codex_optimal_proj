#!/usr/bin/env python3

import sys

def main():
    while True:
        line = sys.stdin.readline()
        if line == "": # EOF
            break
        M, N, C = line.split() # M: number of rows, N: number of columns, C: character to be replaced
        M = int(M)
        N = int(N)
        first = [] # first matrix
        for i in range(M):
            first.append(sys.stdin.readline())
        sys.stdin.readline()
        second = [] # second matrix
        for i in range(M):
            second.append(sys.stdin.readline())
        for i in range(M):
            for j in range(N):
                if second[i][j] == C: # replace
                    sys.stdout.write(first[i][j])
                else:
                    sys.stdout.write(second[i][j])
            sys.stdout.write("\n")
        sys.stdout.write("\n")

if __name__ == "__main__":
    main()
