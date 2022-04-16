import math

import sys

def main():
    n = int(sys.stdin.readline().strip())
    xs = []
    ys = []
    for i in range(n):
        x, y = map(float, sys.stdin.readline().split())
        xs.append(x)
        ys.append(y)
    a = float(sys.stdin.readline().strip())
    dxs = [xs[i+1]-xs[i] for i in range(n-1)] + [xs[0]-xs[n-1]]
    dys = [ys[i+1]-ys[i] for i in range(n-1)] + [ys[0]-ys[n-1]]
    ds = [math.sqrt(dxs[i]**2+dys[i]**2) for i in range(n)]
    d = sum(ds)
    r = a/math.sqrt(d)
    new_xs = [r*dx/ds[i] for i, dx in enumerate(dxs)]
    new_ys = [r*dy/ds[i] for i, dy in enumerate(dys)]
    x_min = min(new_xs)
    y_min = min(new_ys)
    for i in range(n):
        new_xs[i] -= x_min
        new_ys[i] -= y_min
    for i in range(n):
        print(new_xs[i], new_ys[i])

if __name__ == '__main__':
    main()
