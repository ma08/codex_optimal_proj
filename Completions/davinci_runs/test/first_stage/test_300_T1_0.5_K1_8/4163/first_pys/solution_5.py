

import sys
from collections import deque

def main():
    N = int(input())
    q = deque(maxlen=3)

    for i in range(N):
        a, b = map(int, input().split())
        q.append((a, b))
        if len(q) == 3 and q[0][0] == q[0][1] and q[1][0] == q[1][1] and q[2][0] == q[2][1]:
            print("Yes")
            sys.exit()

    print("No")

if __name__ == '__main__':
    main()