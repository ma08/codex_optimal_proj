

import numpy as np
import math

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    x = np.array(x)
    y = np.array(y)
    x_ = np.sum(x) / N
    y_ = np.sum(y) / N
    x_ = np.array([x_ for _ in range(N)])
    y_ = np.array([y_ for _ in range(N)])
    s = np.sum(np.sqrt((x-x_)**2 + (y-y_)**2))
    print(s / N)

if __name__ == '__main__':
    main()
