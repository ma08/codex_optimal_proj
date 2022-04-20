

import sys

def main():
    n, m, s = map(int, input().split())
    roads = []
    for i in range(m):
        u, v = map(int, input().split())
        roads.append((u, v))
    reachable = {s}
    for i in range(m):
        if roads[i][0] in reachable:
            reachable.add(roads[i][1])
    extra = 0
    for i in range(1, n + 1):
        if i not in reachable:
            extra += 1
    print(extra)

if __name__ == "__main__":
    main()