
import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split())

if a == b == c:
    print("YES")
else:
    print("NO")
