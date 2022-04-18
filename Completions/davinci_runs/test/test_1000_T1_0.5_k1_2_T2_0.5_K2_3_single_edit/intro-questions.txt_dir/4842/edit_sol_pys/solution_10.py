#!/usr/bin/env python3

import sys

def print_diff_table(n, v):
    diff_table = [v]
    while len(diff_table[-1]) > 1:
        diff_table.append([])
        for i in range(len(diff_table[-2]) - 1):
            diff_table[-1].append(diff_table[-2][i + 1] - diff_table[-2][i])
    for i in range(len(diff_table)):
        print("\t".join(map(str, diff_table[i])))
    print()

def main():
    n = int(sys.stdin.readline().rstrip())
    v = list(map(int, sys.stdin.readline().rstrip().split()))
    print_diff_table(n, v)

if __name__ == '__main__':
    main()
