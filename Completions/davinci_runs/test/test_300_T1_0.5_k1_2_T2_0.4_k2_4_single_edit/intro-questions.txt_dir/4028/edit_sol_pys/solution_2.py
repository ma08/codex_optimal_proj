
import sys
from collections import deque

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    q = deque()
    for i in range(n):
        while q and q[-1] < a[i]:
            q.pop()
        q.append(a[i])
        if i >= k-1:
            print(q[0], end=' ')
            if q[0] == a[i-k+1]:
                q.popleft()
    print()

if __name__ == "__main__":
    main()
