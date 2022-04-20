

import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    b = [0]*n
    for i in range(n):
        b[a[i]-1] = str(i+1)
    print(' '.join(b))

main()