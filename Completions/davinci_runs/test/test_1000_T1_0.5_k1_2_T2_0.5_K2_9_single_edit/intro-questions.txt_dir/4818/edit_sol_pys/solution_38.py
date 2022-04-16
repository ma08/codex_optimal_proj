
from itertools import accumulate
import sys

def main():
    n = int(sys.stdin.readline().split())
    tasks = list(map(int, sys.stdin.readline().split()))
    free_times = list(map(int, sys.stdin.readline().split()))

    tasks.sort()
    free_times.sort()
    free_times_accum = list(accumulate(free_times))

    print(sum(t <= f for t, f in zip(tasks, free_times_accum)))

if __name__ == '__main__':
    main()
