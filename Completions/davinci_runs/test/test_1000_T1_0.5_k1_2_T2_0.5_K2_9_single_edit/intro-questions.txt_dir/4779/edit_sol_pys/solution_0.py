# python3

import sys

def solve(n, a):
    a.sort()
    result = 0
    cur_sum = 0
    for i in range(n):
        cur_sum += a[i]
        result = max(result, cur_sum * a[i])
    return result

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = []
    for i in range(n):
        a.append(int(sys.stdin.readline()))
    print(solve(n, a))
