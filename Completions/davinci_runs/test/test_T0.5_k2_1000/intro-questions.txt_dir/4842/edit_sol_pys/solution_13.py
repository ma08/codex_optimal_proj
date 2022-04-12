
import sys
import math

def main():
    n = int(sys.stdin.readline())
    v = [int(x) for x in sys.stdin.readline().split()]
    d = [[0 for i in range(n)] for j in range(n - 1)]
    for i in range(n):
        for j in range(i + 1, n):
            d[i][j - 1] = v[j] - v[i]
    for i in range(n - 1):
        if d[i][0] == 0:
            print(i + 1, v[n - 1])
            return

if __name__ == '__main__':
    main()
