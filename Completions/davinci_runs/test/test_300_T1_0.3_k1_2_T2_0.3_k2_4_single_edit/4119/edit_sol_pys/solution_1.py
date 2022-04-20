
import sys


def main():
    # read input from stdin
    n, m = map(int, sys.stdin.readline().split())
    x = list(map(int, sys.stdin.readline().split()))

    # sort the coordinates in ascending order
    x.sort()

    # find the minimum number of moves required to achieve the objective using
    # the greedy algorithm
    ans = 0
    for i in range(m):

        ans += abs(x[i] - x[i - 1])
    print(ans)

if __name__ == '__main__':
    main()
