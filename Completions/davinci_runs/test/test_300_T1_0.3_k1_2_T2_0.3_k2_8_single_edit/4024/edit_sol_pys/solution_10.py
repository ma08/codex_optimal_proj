
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())  # read a line with a single integer
    s = sys.stdin.readline().strip()   # read a list of integers, 2 in this case
    print("{} {}".format(n, k))

if __name__ == "__main__":
    main()
