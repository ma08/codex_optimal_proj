
import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    tasks = list(map(int, sys.stdin.readline().split()))
    intervals = list(map(int, sys.stdin.readline().split()))
    tasks.sort(reverse=True)
    intervals.sort(reverse=True)

    best = 0
    i = 0
    j = 0
    while i < n and j < m:
        if tasks[i] <= intervals[j]:
            best += 1
            i += 1
        j += 1
    print(best)


if __name__ == '__main__':
    main()
