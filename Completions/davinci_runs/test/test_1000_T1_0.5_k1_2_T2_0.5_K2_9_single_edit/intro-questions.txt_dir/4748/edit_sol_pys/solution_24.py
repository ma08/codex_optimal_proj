

import sys

def main():
    h, n, m = [int(x) for x in sys.stdin.readline().split()]
    a = [0]*(h+1)
    b = [0]*(h+1)
    for i in range(1,h+1,1):
        a[i] = 2*i
        b[i] = i
    if sum(a) <= n:
        a = [0]*(h+1)
    else:
        a = [x-n for x in a]
    if sum(b) <= m:
        b = [0]*(h+1)
    else:
        b = [x-m for x in b]
    print(max(a), max(b))

if __name__ == '__main__':
    main()
