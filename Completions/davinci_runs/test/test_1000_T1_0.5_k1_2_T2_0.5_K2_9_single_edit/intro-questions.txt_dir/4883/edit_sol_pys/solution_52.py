

import sys

def main():
    m, n = map(int, sys.stdin.readline().split())
    d = dict()
    for i in range(m):
        a, b = sys.stdin.readline().split()
        if a not in d:
            d[a] = set(b)
        else:
            d[a].add(b)
    for i in range(n):
        a, b = sys.stdin.readline().split()
        if len(a) != len(b):
            print("no")
            continue
        for i in range(len(a)):
            if a[i] in d:
                if b[i] in d[a[i]]:
                    continue
                else:
                    print("no")
                    continue
            else:
                print("no")
                continue
        else:
            print("yes")

main()
