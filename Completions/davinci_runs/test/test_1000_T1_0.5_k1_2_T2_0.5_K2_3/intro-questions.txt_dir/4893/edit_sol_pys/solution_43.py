import numpy as np

n = int(raw_input())

a = np.zeros((n, n))

for i in xrange(n):
    a[i] = map(int, raw_input().split())

a = np.sort(a, axis=0)

for i in xrange(n):
    for j in xrange(n):
        print(int(a[i][j]), end=" ")
    print("")
