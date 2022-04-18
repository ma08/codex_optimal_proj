

import sys

a, b, c = map(int, sys.stdin.readline().split())

if a == 5 and b == 7 and c == 5 and a != b and b != c:
    print("YES")
else:
    print("NO")
