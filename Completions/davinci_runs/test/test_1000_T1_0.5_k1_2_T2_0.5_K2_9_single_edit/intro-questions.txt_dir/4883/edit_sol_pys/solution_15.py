

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
        c, d = sys.stdin.readline().split()
        if len(c) != len(d):
            print("no")
            continue
        c = list(c)
        d = list(d)
        for i in range(len(c)):
            if c[i] in d:
                if d[i] in d[c[i]]:
                    continue
                else:
                    print("no")
                    break
            else:
                print("no")
                break
        else:
            print("yes")

main()
