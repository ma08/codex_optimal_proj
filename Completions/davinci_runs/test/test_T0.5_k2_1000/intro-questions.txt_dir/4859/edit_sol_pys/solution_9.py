

import sys

def possible(b, d, c, l, m):
    for i in range(0, m/b + 1):
        for j in range(0, m/d + 1):
            for k in range(0, m/c + 1):
                if i*b + j*d + k*c == m:
                    print i, j, k

def main():
    lines = sys.stdin.readlines()
    b, d, c, l, m = map(int, lines[0].strip().split(' '))
    possible(b, d, c, l, m)

if __name__ == '__main__':
    main()
