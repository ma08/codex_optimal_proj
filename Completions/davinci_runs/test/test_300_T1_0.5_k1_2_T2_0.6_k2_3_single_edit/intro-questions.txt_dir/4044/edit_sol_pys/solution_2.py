
import random

a, b, x = map(int, input().split())

s = []
for i in range(a):
    s.append('0')
for i in range(b):
    s.append('1')

for i in range(0, x, 2):
    s[i], s[i+1] = s[i+1], s[i]
    s[-i-1], s[-i-2] = s[-i-2], s[-i-1]

print(''.join(s))
