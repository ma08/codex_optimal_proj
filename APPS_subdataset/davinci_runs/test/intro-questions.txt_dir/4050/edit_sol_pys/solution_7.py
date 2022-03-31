
from sys import stdin
from collections import defaultdict


def solve(n, array):
    sums = defaultdict(list)  # type: dict
    for i in range(n):
        for j in range(i, n):
            s = sum(array[i:j + 1])
            sums[s].append((i + 1, j + 1))
    best = max(sums.keys())

    return sums[best]

if __name__ == '__main__':
    n = int(stdin.readline())
    array = [int(x) for x in stdin.readline().split()]
    print(len(solve(n, array)))
    for (l, r) in solve(n, array):
        print(l, r)
