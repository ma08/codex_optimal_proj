
from collections import deque
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    a.sort()
    b.sort()
    q = deque(b)
    ans = 0
    for i in range(n):
        while q and q[0] < a[i]:
            q.popleft()
        if q:
            ans += 1
            q.popleft()
    print(ans)

main()
