

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    segs = []
    from collections import defaultdict
    for i in range(m):
        l, r = map(int, sys.stdin.readline().split())
        segs.append((l, r))

    segs.sort(key=lambda x: x[1])

    # print n, m
    # print a
    # print segs

    b = a[:] # copy a
    s = set()
    d = defaultdict(int) # dict to store the number of times a segment appears
    cur = 0
    while cur < m:
        # print 'cur', cur
        # print 's', s
        # print 'b', b
        if len(s) == 0 or segs[cur][0] > segs[s[-1]][1]:
            s.add(cur)
            d[cur] += 1
            for i in range(segs[cur][0], segs[cur][1]+1):
                b[i-1] -= 1
        cur += 1

    print max(b) - min(b)
    print len(d)
    for k in d:
        print k+1, d[k]

if __name__ == "__main__":
    main()
