

import sys

def main():
    s = int(sys.stdin.readline())
    print("%d:" % s)
    for x in range(2, s):
        if (s % x == 0) and ((s // x) > 1) and ((s // x) != x):
            print("%d,%d" % (x, s // x))

if __name__ == '__main__':
    main()
