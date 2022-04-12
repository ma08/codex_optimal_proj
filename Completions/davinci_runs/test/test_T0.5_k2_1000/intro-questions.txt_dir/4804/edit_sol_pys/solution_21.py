
import sys

def main():
    s = int(sys.stdin.readline().strip())
    print("%d:" % s)
    for x in range(2, s):
        if (s % x == 0) and ((s // x) > 1):
            print("%d,%d" % (x, s // x))

if __name__ == '__main__':
    main()
