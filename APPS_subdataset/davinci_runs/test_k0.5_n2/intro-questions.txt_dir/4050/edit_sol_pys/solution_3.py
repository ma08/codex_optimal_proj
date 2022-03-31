
from sys import stdin
from collections import defaultdict


def solve(n, array):
    sums = defaultdict(int)
    for i in range(n):
        for j in range(i, n):
            s = sum(array[i:j+1])
            sums[s] += 1
    best = max(sums.keys())
    return best, sums[best]

if __name__ == '__main__':
    n = int(stdin.readline())
    array = [int(x) for x in stdin.readline().split()]
    print(solve(n, array))
