

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
        for i in range(len(a) - 1):
            if a[i:i+2] in d:
                if b[i:i+2] in d[a[i:i+2]]:
                    continue
                else:
                    print("no")
                    break
        else:
            print("yes")

main()
