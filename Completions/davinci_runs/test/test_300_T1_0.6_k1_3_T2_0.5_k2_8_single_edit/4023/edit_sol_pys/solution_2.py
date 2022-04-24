
import sys
#-----Solution-----

a = input().split()
b = input().split()

n = int(a[0])
m = int(b[0])

if n != m:
    print('NO')
    sys.exit()

for i in range(n-1):
    if b[i] != b[i+1]:
        print('NO')
        sys.exit()

print('YES')
