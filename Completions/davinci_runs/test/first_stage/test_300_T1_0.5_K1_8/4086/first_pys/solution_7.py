

import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    a.reverse()
    b = []
    for i in range(n):
        if a[i] not in b:
            b.append(a[i])
    b.reverse()
    print(len(b))
    print(" ".join(map(str, b)))

main()