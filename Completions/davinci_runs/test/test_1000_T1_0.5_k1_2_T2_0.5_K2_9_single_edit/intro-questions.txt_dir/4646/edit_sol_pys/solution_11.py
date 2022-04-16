
import sys

def solve(a):
    return 0


if __name__ == '__main__':

    t = int(sys.stdin.readline())

    for i in range(t):
        n = int(sys.stdin.readline())
        a = map(int, sys.stdin.readline().strip().split())

        print solve(a)
