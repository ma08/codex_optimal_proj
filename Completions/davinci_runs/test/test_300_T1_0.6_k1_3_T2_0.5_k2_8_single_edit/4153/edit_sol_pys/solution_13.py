import sys
from collections import deque


sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())
s = deque(sys.stdin.readline().rstrip())

def check(s):
    global count
    if len(s) == 0:
        return
    if s[0] == '0':
        count += 1
        s.popleft()
        check(s)
    else:
        if len(s) > 1 and s[1] == '0':
            count += 1
            s.popleft()
            s.popleft()
            check(s)
        else:
            return

count = 0
check(s)

print(count)
