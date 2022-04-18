
import sys
import math

def main():
    n, m = map(int, input().split())
    tasks = map(int, input().split())
    intervals = map(int, input().split())
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
