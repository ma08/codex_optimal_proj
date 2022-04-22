import sys

n,a,b = map(int,input().split())

if a > b:
    a,b = b,a

if a == 0:
    sys.stdout.write(str(0))
else:
    sys.stdout.write(str(min(n,a)))
