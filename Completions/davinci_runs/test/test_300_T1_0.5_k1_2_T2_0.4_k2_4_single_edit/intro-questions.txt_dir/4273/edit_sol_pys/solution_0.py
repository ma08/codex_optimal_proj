
import sys

def main():
    N = int(sys.stdin.readline())  # read a line with a single integer
    for i in xrange(1, N + 1):
        s = sys.stdin.readline().strip()
        print "Case #{}: {}".format(i, solve(s))


if __name__ == '__main__':
    main()
