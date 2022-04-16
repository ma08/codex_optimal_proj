

import os
import sys

def solve(n, m, k, l):
    # if there are more than k + 1 files, it is impossible
    # if there are k + 1 files, then the answer is the number of files - 1
    # otherwise, the answer is the number of files
    if n > k + 1:
        return -1
    elif n == k + 1:
        return n - 1
    else:
        return n

def main():
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    k = int(sys.stdin.readline().strip())
    l = int(sys.stdin.readline().strip())
    print(solve(n, m, k, l))

if __name__ == "__main__":
    main()
