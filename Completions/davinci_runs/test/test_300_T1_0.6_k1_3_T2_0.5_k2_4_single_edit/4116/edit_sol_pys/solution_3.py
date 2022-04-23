

import sys
from collections import deque
input = sys.stdin.readline

def main():
    N = int(input())
    d = deque()
    for _ in range(N):
        cmd, *args = input().split()
        if cmd == "insert":
            d.appendleft(args[0])
        elif cmd == "delete":
            if args[0] in d:
                d.remove(args[0])
        elif cmd == "deleteFirst":
            d.popleft()
        elif cmd == "deleteLast":
            d.pop()
    print(*d)

main()
