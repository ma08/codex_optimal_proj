from collections import defaultdict
import sys
from collections import deque

def main():
    m, n = map(int, sys.stdin.readline().split())
    d = defaultdict(set)
    for _ in range(m):
        a, b = sys.stdin.readline().split()
        d[a].add(b)
    for _ in range(n):
        a, b = sys.stdin.readline().split()
        if len(a) != len(b):
            print("no")
            continue
        a = list(a)
        b = list(b)
        q = deque()
        visited = set()
        q.append((0, a[0], b[0]))
        while q:
            i, c1, c2 = q.popleft()
            if i == len(a) - 1:
                if c1 == c2:
                    print("yes")
                    break
                else:
                    print("no")
                    break
            if (i, c1, c2) in visited:
                continue
            visited.add((i, c1, c2))
            if c1 == c2:
                q.append((i + 1, a[i + 1], b[i + 1]))
            else:
                if c1 in d:
                    for c in d[c1]:
                        q.append((i, c, c2))
                if c2 in d:
                    for c in d[c2]:
                        q.append((i, c1, c))


main()
