

import sys

def main():
    n = int(input())
    segments = []
    for i in range(n):
        s = [int(x) for x in input().split()]
        segments.append(s)
    segments.sort(key=lambda x:x[0])
    i = 0
    while i < n - 1:
        if segments[i][1] < segments[i + 1][0]:
            del segments[i + 1]
            n -= 1
        elif segments[i][1] < segments[i + 1][1]:
            del segments[i + 1]
            n -= 1
        else:
            i += 1
    segs = [0] * n
    for i in range(n):
        segs[i] = segments[i][1] - segments[i][0]
    segs.sort()
    if n > 1:
        print(segs[n - 2])
    else:
        print(0)

main()
