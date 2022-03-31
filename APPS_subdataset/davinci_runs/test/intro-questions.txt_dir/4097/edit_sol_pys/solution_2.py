
import sys

n = int(sys.stdin.readline().strip())
b = [int(x) for x in sys.stdin.readline().strip().split()]
b.sort()
if len(b) == 1:
    print(0)
    sys.exit(0)
if b[1] - b[0] == 0:
    print(1)
    sys.exit(0)
if b[1] - b[0] == 1:
    print(0)
    sys.exit(0)
if b[1] - b[0] > 1:
    print(-1)
    sys.exit(0)
if b[9] - b[8] == 1:
    print(8)
    sys.exit(0)
if b[9] - b[8] == 0:
    print(9)
    sys.exit(0)
if b[9] - b[8] > 1:
    print(-1)
    sys.exit(0)
print(0)
