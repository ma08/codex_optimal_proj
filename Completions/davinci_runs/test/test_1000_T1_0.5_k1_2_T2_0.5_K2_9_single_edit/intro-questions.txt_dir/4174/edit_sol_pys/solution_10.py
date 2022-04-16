import sys
from collections import deque


input = sys.stdin.readline

n = int(input())
q = deque()

for i in range(n):
    inp = input().rstrip()

    if inp.startswith("push"):
        _, x = inp.split()
        q.append(x)
    elif inp == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif inp == "size":
        print(len(q))
    elif inp == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif inp == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif inp == "back":
        if q:
            print(q[-1])
        else:
            print(-1)

