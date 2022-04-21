
import sys

n, x, y = map(int, input().split())
n = str(input())

if n[y-1] == '0':
    n = list(n)
    n[y-1] = '1'
else:
    n = list(n)
    n[y-1] = '0'
    for i in range(y+1, x):
        if n[i] == '0':
            n[i] = '1'
            break
        else:
            n[i] = '0'

print(n.count('0'))
