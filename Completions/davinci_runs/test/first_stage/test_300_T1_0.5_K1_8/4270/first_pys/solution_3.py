

import sys

def main():
    n = int(sys.stdin.readline().strip())
    v = [int(x) for x in sys.stdin.readline().strip().split()]
    v.sort()
    while n > 1:
        x = v[0]
        y = v[1]
        v[0] = (x + y) / 2
        v.remove(y)
        n -= 1
    print(v[0])

if __name__ == '__main__':
    main()