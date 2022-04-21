
import collections
import sys

def main():
    n = int(sys.stdin.readline().strip())
    a = sys.stdin.readline().strip().split()
    d = collections.defaultdict(int)
    for i in a:
        d[i] += 1
    print(max(d.values()))

if __name__ == "__main__":
    main()
