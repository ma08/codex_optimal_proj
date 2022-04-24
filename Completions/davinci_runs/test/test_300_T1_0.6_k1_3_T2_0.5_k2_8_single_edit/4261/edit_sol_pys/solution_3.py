
import sys
a, b, c = map(int, input().split())

while 1:
    if b + c <= a:
        sys.stdout.write(str(0))
        break
    elif b + c > a:
        sys.stdout.write(str(b + c - a))
        break
