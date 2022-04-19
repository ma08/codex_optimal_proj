
import math
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = [0] * n
    for i in range(m):
        a[i % n] += 1
    print(max(a))

if __name__ == '__main__':
    main()
