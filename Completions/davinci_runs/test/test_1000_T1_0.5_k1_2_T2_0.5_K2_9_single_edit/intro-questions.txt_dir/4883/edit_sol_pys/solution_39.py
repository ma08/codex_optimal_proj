import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    lookup = {}
    for _ in range(n):
        a, b = sys.stdin.readline().split()
        lookup[a] = b
    for i in range(m):
        c, d = sys.stdin.readline().split()
        if len(c) != len(d):
            print("no")
            continue
        for j in range(len(c)):
            if c[j] not in lookup or lookup[c[j]] != d[j]:
                print("no")
                break
        print("yes")

main()
