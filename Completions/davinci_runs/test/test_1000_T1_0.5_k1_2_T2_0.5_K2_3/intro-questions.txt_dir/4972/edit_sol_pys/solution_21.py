
import sys
import math

def main():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    a.sort()
    m = float(a[0])
    for i in range(1, n):
        m = (m + float(a[i]))/2
    print(m)

if __name__ == '__main__':
    main()
