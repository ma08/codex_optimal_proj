#!/usr/bin/env python3

import sys

def main():
    n, m = tuple(int(i) for i in sys.stdin.readline().split())
    times = [tuple(int(i) for i in sys.stdin.readline().split()) for i in range(n)]
    mowers = [(i,j) for i in range(n) for j in range(m)]
    mowers = sorted(mowers, key=lambda x: times[x[0]][x[1]], reverse=True)
    completed = [None]*n
    while mowers:
        i, j = mowers.pop(0)
        if j == 0:
            completed[i] = times[i][0]
        elif completed[i-1] is None:
            mowers.append((i, j))
        else:
            completed[i] = max(completed[i-1], completed[i]) + times[i][j]
    print(' '.join(str(i) for i in completed))

if __name__ == '__main__':
    main()
