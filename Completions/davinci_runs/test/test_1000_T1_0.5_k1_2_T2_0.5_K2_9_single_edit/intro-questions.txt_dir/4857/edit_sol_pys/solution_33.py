

import sys

l, w = map(int, input().split())

if w > 26 * l:
    print("impossible")
    sys.exit()

if w > 26 * (l - 1) + 1:
    print("impossible")
    sys.exit()
else:
    print(chr(w - 26 * (l - 1) + 96), end = "")
    w -= w - 26 * (l - 1) + 1

if w > 26 * (l - 2) + 2:
    print("impossible")
    sys.exit()
else:
    print(chr(w - 26 * (l - 2) + 96), end = "")
    w -= w - 26 * (l - 2) + 2

for i in range(3, l + 1):
    if w > 26 * (l - i) + i:
        print("impossible")
        sys.exit()
    else:
        print(chr(w - 26 * (l - i) + 96), end = "")
        w -= w - 26 * (l - i) + i

print("a" * (l - i))
