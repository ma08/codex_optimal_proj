
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

if len(set(a)) == n:  # set은 중복을 제거한다.
    print("YES")
else:
    print("NO")
