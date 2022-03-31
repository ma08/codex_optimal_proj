
import sys

n = int(sys.stdin.readline().strip())
b = [int(x) for x in sys.stdin.readline().strip().split()]
if len(b) < 3:
    print(0)
    sys.exit(0)
b.sort()
if len(b) == 1:
    print(0)
    sys.exit(0)
if len(b) == 2:
    if b[1] - b[0] == 1:
        print(1)
    elif b[1] - b[0] == 0:
        print(0)
    else:
        print(-1)
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
# if b[1] - b[0] == 0:
#     if b[2] - b[1] == 1:
#         print(2)
#     elif b[2] - b[1] == 0:
#         print(1)
#     else:
#         print(-1)
#     sys.exit(0)
if b[2] - b[1] == 1:
    print(1)
    sys.exit(0)
if b[2] - b[1] > 1:
    print(-1)
    sys.exit(0)
if b[2] - b[1] == 0:
    print(2)
    sys.exit(0)
if b[2] - b[1] == 0:
    if b[3] - b[2] == 1:
        print(3)
    elif b[3] - b[2] == 0:
        print(2)
    else:
        print(-1)
    sys.exit(0)
if b[3] - b[2] == 1:
    print(2)
    sys.exit(0)
if b[3] - b[2] == 0:
    print(3)
    sys.exit(0)
if b[3] - b[2] > 1:
    print(-1)
    sys.exit(0)
if b[4] - b[3] == 1:
    print(3)
    sys.exit(0)
if b[4] - b[3] == 0:
    print(4)
    sys.exit(0)
if b[4] - b[3] > 1:
    print(-1)
    sys.exit(0)
if b[5] - b[4] == 1:
    print(4)
    sys.exit(0)
if b[5] - b[4] == 0:
    print(5)
    sys.exit(0)
if b[5] - b[4] > 1:
    print(-1)
    sys.exit(0)
if b[6] - b[5] == 1:
    print(5)
    sys.exit(0)
if b[6] - b[5] == 0:
    print(6)
    sys.exit(0)
if b[6] - b[5] > 1:
    print(-1)
    sys.exit(0)
if b[7] - b[6] == 1:
    print(6)
    sys.exit(0)
if b[7] - b[6] == 0:
    print(7)
    sys.exit(0)
if b[7] - b[6] > 1:
    print(-1)
    sys.exit(0)
if b[8] - b[7] == 1:
    print(7)
    sys.exit(0)
if b[8] - b[7] == 0:
    print(8)
    sys.exit(0)
if b[8] - b[7] > 1:
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
