#-----Solution-----


import sys

a = input().split()
b = input().split()

n = int(a[0])
m = int(b[0])

if n != m:
    sys.exit(print('NO'))

for i in range(n-1):
    if b[i] != b[i+1]:
        sys.exit(print('NO'))

print('YES')
