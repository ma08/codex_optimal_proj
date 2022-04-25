
import sys

def main():
    n = int(sys.stdin.readline()) # read a line with a single integer
    a = list(map(int, sys.stdin.readline().split())) # read a list of integers, 2 in this case
    print(solve(n, a))

def solve(n, a):
    return 0

if __name__ == '__main__':
    main()
