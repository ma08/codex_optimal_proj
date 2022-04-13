import sys
from collections import Counter


def solve(n, v):
    c = Counter(v)
    if len(c) == 1:
        return n, v[0] * n
    v_diff = []
    for i in range(n - 1):
        v_diff.append(v[i + 1] - v[i])
    return solve(n - 1, v_diff)


def main():
    n = int(sys.stdin.readline())
    v = list(map(int, sys.stdin.readline().split()))
    d = 0
    while True:
        d += 1
        v_diff = []
        for i in range(len(v) - 1):
            v_diff.append(v[i + 1] - v[i])
        v = v_diff
        if len(set(v)) == 1:
            break
    print(d, v[0] * d + v[0])

if __name__ == '__main__':
    main()
