
import sys

def main():
    m, n = map(int, sys.stdin.readline().split())
    d = {}
    for i in range(m):
        a, b = sys.stdin.readline().split()
        if a not in d:
            d[a] = [b]
        else:
            d[a].append(b)
    for i in range(n):
        a, b = sys.stdin.readline().split()
        if len(a) != len(b):
            print("no")
            continue
        if a[0] in d:
            if b[0] in d[a[0]]:
                print("yes")
            else:
                print("no")
        else:
            print("yes")

main()
