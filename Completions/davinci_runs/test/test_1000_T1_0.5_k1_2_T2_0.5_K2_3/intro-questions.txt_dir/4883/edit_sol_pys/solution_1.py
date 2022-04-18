

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
        flag = True
        a, b = sys.stdin.readline().split()
        a = list(a)
        b = list(b)
        if len(a) == len(b):
            for i in range(len(a)):
                if a[i] in d:
                    if b[i] in d[a[i]]:
                        continue
                    else:
                        flag = False
                else:
                    flag = False
        if flag:
            print("yes")
        else: print("no")

main()
