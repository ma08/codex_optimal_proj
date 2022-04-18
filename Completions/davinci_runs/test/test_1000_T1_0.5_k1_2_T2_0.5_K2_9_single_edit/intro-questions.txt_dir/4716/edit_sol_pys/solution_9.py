import numpy as np
import scipy.sparse.csgraph as cs


def main():
    n, m = map(int, input().split())
    # l = list(map(int, input().split()))
    # l.sort(reverse=True)
    # print(sum(l[:k]))
    # print(np.zeros(n))
    print(cs.floyd_warshall(np.zeros(n)))


if __name__ == '__main__':
    main()
