
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    s = list(map(int, sys.stdin.readline().strip().split()))
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    t = []
    while len(t) < k:
        m = max(d, key=d.get)
        t.append(m)
        d[m] -= 1
        if d[m] == 0:
            del d[m]
    print(' '.join(map(str, t)))

if __name__ == '__main__':
    main()
