

import sys

def possible(l, b, d, c):
    max_b = l/b + 1
    max_d = l/d + 1
    max_c = l/c + 1
    for i in xrange(0, max_b):
        for j in xrange(0, max_d):
            for k in xrange(0, max_c):
                if i*b + j*d + k*c == l:
                    print(i, j, k)

def main():
    lines = sys.stdin.readlines()
    b, d, c, l = map(int, lines[0].strip().split(' '))
    possible(l, b, d, c)

if __name__ == '__main__':
    main()
