
import sys

n = str(n)
n = list(n)
length = len(n)
pos = 0
while pos < length - 1:
    if n[pos] == '0' and n[pos + 1] != '0':
        n[pos], n[pos + 1] = n[pos + 1], n[pos]
        pos += 2
    else:
        pos += 1
n = ''.join(n)
if int(n) % 25 == 0:
    print(length - len(n))
else:
    print(-1)
n = int(sys.stdin.readline())
