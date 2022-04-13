"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0018
"""

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
        for j in range(len(a)):
            if a[j] in d:
                if b[j] in d[a[j]]:
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
