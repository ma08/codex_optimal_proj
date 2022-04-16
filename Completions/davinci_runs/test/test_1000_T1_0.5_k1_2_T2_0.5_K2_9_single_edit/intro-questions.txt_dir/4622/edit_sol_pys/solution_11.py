
#
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

if len(set(a)) == n:
    print("YES")
else:
    print("NO")
