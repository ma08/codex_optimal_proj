
import os
import sys

def main():
    with open('input.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        a = list(map(int, f.readline().split()))
        segments = []
        for i in range(m):
            l, r = map(int, f.readline().split())
            segments.append((l, r))
        segments.sort(key=lambda x: x[1] - x[0])
        ans = 0
        for i in range(m):
            l, r = segments[i]
            if a[l - 1] > a[r - 1]:
                a[l - 1], a[r - 1] = a[r - 1], a[l - 1]
            ans = max(ans, a[l - 1] - a[r - 1])
        with open('output.txt', 'w') as g:
            g.write(str(ans) + '\n')
            g.write(str(0))

if __name__ == '__main__':
    main()
