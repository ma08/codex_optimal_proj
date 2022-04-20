
from collections import Counter
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    s = list(map(int, sys.stdin.readline().split()))
    d = Counter(s)
    t = []
    while len(t) < k:
        m = max(d, key=d.get)
        t.append(m)
        d[m] -= 1
        if d[m] == 0:
            del d[m]
    print(*t)

if __name__ == '__main__':
    main()
