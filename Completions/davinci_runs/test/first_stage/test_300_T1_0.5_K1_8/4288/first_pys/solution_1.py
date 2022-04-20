

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if a == b and b != c:
    print("Yes")
elif a == c and c != b:
    print("Yes")
elif b == c and c != a:
    print("Yes")
else:
    print("No")