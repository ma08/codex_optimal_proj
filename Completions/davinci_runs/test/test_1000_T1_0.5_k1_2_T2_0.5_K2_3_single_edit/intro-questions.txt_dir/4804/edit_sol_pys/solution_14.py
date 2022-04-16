

import sys

def main():
    s = sys.stdin.readline()
    print("%s:" % s)
    for x in range(2, int(s)):
        if (int(s) % x == 0) and ((int(s) // x) > 1):
            print("%d,%d" % (x, int(s) // x))

if __name__ == '__main__':
    main()
