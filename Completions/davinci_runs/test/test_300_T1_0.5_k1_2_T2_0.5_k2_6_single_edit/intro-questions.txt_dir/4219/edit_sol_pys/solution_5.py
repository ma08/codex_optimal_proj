
from collections import defaultdict
import sys

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]

    # read edges
    edges = defaultdict(list)
    for i in range(m):
        a, b = [int(x) for x in sys.stdin.readline().split()]
        edges[a].append(b)
        edges[b].append(a)

if __name__ == '__main__':
    main()
