
from sys import stdin
from collections import defaultdict

def solve(n, arr):
    sums = defaultdict(list)
    for i in range(n):
        for j in range(i, n):
            s = sum(arr[i:j+1])
            sums[s].append((i+1, j+1))
    best = max(sums.keys())
    return sums[best][0]

if __name__ == '__main__':
    n = int(stdin.readline())
    arr = [int(x) for x in stdin.readline().split()]
    (l, r) = solve(n, arr)
    print(l, r)
