import sys

n, w = map(int, input().split())
a = list(map(int, input().split()))

i = 0
j = 0

for i in range(n):
    if a[i] > w or a[i] < -w:
        sys.stdout.write(str(0))
        break
    j += a[i]
    if j > w or j < 0:
        sys.stdout.write(str(0))
        break

if i == n-1:
    sys.stdout.write(str(w-j+1))
