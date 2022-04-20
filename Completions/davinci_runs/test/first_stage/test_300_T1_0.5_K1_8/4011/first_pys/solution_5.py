

import sys

def solve(n, a, f):
    a = list(a)
    max_num = int(''.join(a))
    for i in range(n):
        for j in range(i, n):
            b = a[:]
            for k in range(i, j + 1):
                b[k] = str(f[int(b[k]) - 1])
            max_num = max(max_num, int(''.join(b)))
    return max_num

n = int(sys.stdin.readline())
a = sys.stdin.readline().strip()
f = [int(x) for x in sys.stdin.readline().split()]

print(solve(n, a, f))