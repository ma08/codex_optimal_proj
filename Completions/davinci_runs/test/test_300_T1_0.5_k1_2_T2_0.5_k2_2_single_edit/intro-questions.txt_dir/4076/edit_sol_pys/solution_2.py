
import sys
n = int(sys.stdin.readline())

arr = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    arr[i] = sys.stdin.readline().split()

for i in range(n):
    for j in range(n):
        arr[i][j] = int(arr[i][j])

print(arr)
