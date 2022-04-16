

import sys

def possible(b, d, c, l):
    for i in xrange(0, l/b + 1):
        for j in xrange(0, l/d + 1):
            for k in xrange(0, l/c + 1):
                if i*b + j*d + k*c == l:
                    print(i, j, k)

def main():
    lines = sys.stdin.readlines()
    b, d, c, l = map(int, lines[0].strip().split(' '))
    possible(b, d, c, l)

if __name__ == '__main__':
    main()
