

import sys

def min_shovels(n, k):
    if n == k:
        return 1
    elif k > n:
        return n
    else:
        return n//k + min_shovels(n%k, k)

# Main
t = [int(i) for i in sys.stdin.readline().strip().split()][0]

for i in range(t):
    n, k = [int(i) for i in sys.stdin.readline().strip().split()]
    print(min_shovels(n, k))