
import sys
import math

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    tasks = map(int, sys.stdin.readline().split())
    intervals = map(int, sys.stdin.readline().split())
    tasks.sort()
    intervals.sort()
    tasks.append(math.inf)
    intervals.append(math.inf)
    i = 0
    j = 0
    count = 0
    while i < n and j < m:
        if tasks[i] <= intervals[j]:
            count += 1
            i += 1
        j += 1
    print(count)

main()
