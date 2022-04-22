

import sys

n, m = [int(i) for i in sys.stdin.readline().split()]
arr = []
for i in range(n):
    arr.append([int(i) for i in sys.stdin.readline().split()])
    arr[i].sort()
    row = arr[i]
    for j in range(m-1):
        row[j] = row[j+1] - row[j]
    row.pop()
    row.sort()
    print(sum(row[:m-1]))
