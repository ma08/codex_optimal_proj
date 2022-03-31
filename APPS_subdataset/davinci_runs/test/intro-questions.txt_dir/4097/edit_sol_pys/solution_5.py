
import sys

n = int(sys.stdin.readline().strip())
a = [int(x) for x in sys.stdin.readline().strip().split()]

a.sort()

if len(a) == 1:
    print(0)
    sys.exit(0)

if a[1] - a[0] == 0:
    print(1)
    sys.exit(0)

if a[1] - a[0] == 1:
    print(0)
    sys.exit(0)

if a[1] - a[0] > 1:
    print(-1)
    sys.exit(0)

if a[9] - a[8] == 1:
    print(8)
    sys.exit(0)

if a[9] - a[8] == 0:
    print(9)
    sys.exit(0)

if a[9] - a[8] > 1:
    print(-1)
    sys.exit(0)

print(0)
