
import sys

def main():
    n = int(sys.stdin.readline().rstrip())  # read a line with a single integer
    for i in xrange(1, n + 1):
        a, b = [int(s) for s in sys.stdin.readline().split(" ")]  # read a list of integers, 2 in this case
        print "Case #{}: {} + {} = {}".format(i, a, b, a + b)

if __name__ == "__main__":
    main()
