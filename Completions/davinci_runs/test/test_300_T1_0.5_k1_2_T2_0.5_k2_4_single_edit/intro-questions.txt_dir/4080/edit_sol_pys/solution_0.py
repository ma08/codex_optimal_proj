
import sys

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    a = [int(x) for x in sys.stdin.readline().split()]
    segs = []

    for i in range(m):
        l, r = [int(x) for x in sys.stdin.readline().split()]
        segs.append((l, r))

    segs.sort(key=lambda x: x[1])

    # print n, m
    # print a
    # print segs

    b = a[:]
    s = set()
    cur = 0
    while cur < m:
        # print 'cur', cur
        # print 's', s
        # print 'b', b
        if len(s) == 0 or segs[cur][0] > segs[s[-1]][1]:
            s.add(cur)
            for i in range(segs[cur][0], segs[cur][1]+1):
                b[i-1] -= 1
        cur += 1

    print(max(b) - min(b))
    print(len(s))
    for i in s:
        print(i+1, end=" ")

if __name__ == "__main__":
    main()
