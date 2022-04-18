
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    lookup = {}
    for _ in range(n):
        a, b = sys.stdin.readline().split()
        lookup[a] = b
    for i in range(m):
        a, b = sys.stdin.readline().split()
        if len(a) != len(b):
            print("no")
            continue
        for j in range(len(a)):
            if a[j] not in lookup or lookup[a[j]] != b[j]:
                print("no")
        else:
            print("yes")
                break
        else:
            print("yes")

main()
