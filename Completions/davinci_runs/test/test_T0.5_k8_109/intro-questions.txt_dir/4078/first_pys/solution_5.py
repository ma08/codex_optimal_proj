

import numpy as np

def main():
    n, m = map(int, input().split())
    a = np.array(list(map(int, input().split())))
    segments = []
    for i in range(m):
        l, r = map(int, input().split())
        segments.append((l-1, r-1))
    d = 0
    q = 0
    c = []
    for s in segments:
        if np.max(a[s[0]:s[1]+1]) - np.min(a[s[0]:s[1]+1]) > d:
            d = np.max(a[s[0]:s[1]+1]) - np.min(a[s[0]:s[1]+1])
            q = 1
            c = [segments.index(s)+1]
        elif np.max(a[s[0]:s[1]+1]) - np.min(a[s[0]:s[1]+1]) == d:
            q += 1
            c.append(segments.index(s)+1)
    print(d)
    print(q)
    print(*c)

if __name__ == '__main__':
    main()