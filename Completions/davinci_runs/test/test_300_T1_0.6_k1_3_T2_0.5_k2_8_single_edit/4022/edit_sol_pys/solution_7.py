

import sys, math

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    a = [0] * n
    for i in range(n): a[i] = int(sys.stdin.readline())
    a.sort()
    min = a[n - 1] - a[0]
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[j] - a[i] < min: min = a[j] - a[i]
            if a[j] - a[i] >= m: break
    print(min)

main()
