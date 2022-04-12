
import sys

def main():
    n = int(sys.stdin.readline().strip()) # read a line with a single integer
    for i in xrange(1, n + 1):
        print "Case #{}: {}".format(i, solve(read()))

def read():
    return sys.stdin.readline().strip()

def solve(s):
    return s

if __name__ == "__main__":
    main()
