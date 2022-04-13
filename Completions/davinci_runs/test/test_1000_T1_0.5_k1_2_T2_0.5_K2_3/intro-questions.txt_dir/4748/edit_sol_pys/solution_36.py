

import sys

def main():
    h, n, m = [int(x) for x in sys.stdin.readline().split()]
    a = b = 0
    for i in range(1, h+1):
        a += 2 * i
        b += i
    print(max(a-n, 0), max(b-m, 0))

if __name__ == '__main__':
    main()
