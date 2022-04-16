
import sys

def solve(a, b):
    # Write your code here
    pass

if __name__ == '__main__':

    t = int(sys.stdin.readline())

    for i in range(t):
        n = int(sys.stdin.readline())
        a = map(int, sys.stdin.readline().strip().split())[:n]
        b = map(int, sys.stdin.readline().strip().split())[:n]

        print solve(a, b)
