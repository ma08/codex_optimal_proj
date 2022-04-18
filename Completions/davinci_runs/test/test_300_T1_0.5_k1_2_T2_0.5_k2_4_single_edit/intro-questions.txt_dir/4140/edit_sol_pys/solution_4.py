
import sys
from sys import stdin

s = stdin.readline().strip()
n = int(stdin.readline().strip())
a = list(map(int, stdin.readline().strip().split()))
b = list(map(int, stdin.readline().strip().split()))
c = list(map(int, stdin.readline().strip().split()))
count = 0
for i in range(n - 1):
    if a[i + 1] - a[i] == 1:
        count += b[a[i] - 1] + c[a[i + 1] - 1]
print(count)
