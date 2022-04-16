

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = map(int, sys.stdin.readline().split())
    segs = []
    for i in range(m):
        l, r = map(int, sys.stdin.readline().split())
        segs.append((l-1, r-1))

    segs.sort(key=lambda x: x[1])

    segs.sort(key=lambda x: x[1])
    # print n, m
    # print a
    # print segs
    s = []
    cur = 0
    while cur < m:
        # print 'cur', cur
        if len(s) == 0 or segs[cur][0] > segs[s[-1]][1]: # if not overlapped
            s.append(cur)
            for i in range(segs[cur][0], segs[cur][1]+1): # update a
                a[i] -= 1
        cur += 1

    print max(a) - min(a)
    print len(s)
    for i in s:
        print i+1,

if __name__ == "__main__":
    main()
