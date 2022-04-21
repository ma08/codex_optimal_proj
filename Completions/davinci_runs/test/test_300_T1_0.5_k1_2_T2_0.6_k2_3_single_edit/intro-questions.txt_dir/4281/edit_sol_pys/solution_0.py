import sys


n, k = [int(i) for i in sys.stdin.readline().split()]
a = [int(i) for i in sys.stdin.readline().split()]

cnt = 0
curr = 0

for i in range(n):
    if curr + a[i] <= k:
        curr += a[i]
        cnt += 1
    else:
        break
print(cnt)
