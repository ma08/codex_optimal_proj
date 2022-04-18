

import sys

def possible(l, b, d, c):
    for i in range(0, l//b + 1):
        for j in range(0, l//d + 1):
            for k in range(0, l//c + 1):
                if i*b + j*d + k*c == l:
                    print i, j, k

def main():
    lines = sys.stdin.readlines()
    b, d, c, l = map(int, lines[0].strip().split(' '))
    possible(l, b, d, c)

if __name__ == '__main__':
    main()
