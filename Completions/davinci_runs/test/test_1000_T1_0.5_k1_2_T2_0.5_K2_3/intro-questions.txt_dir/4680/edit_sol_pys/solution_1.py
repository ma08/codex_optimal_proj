
import sys

a, b, c = map(int, sys.stdin.readline().split())

if a == b and b == c:
    print("YES")
else:
    print("NO")
