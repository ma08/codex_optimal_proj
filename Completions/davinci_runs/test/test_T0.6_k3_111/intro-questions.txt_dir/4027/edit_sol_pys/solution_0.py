
import sys
import math

def minDiff(m):
    if m % 2 == 0:
        return m // 2
    else:
        return 1

if __name__ == '__main__':
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        m = int(sys.stdin.readline().strip())
        print(minDiff(m))
