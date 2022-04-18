import math

import sys

def main(n, m):
    task_times = [0] * n
    quiet_times = [0] * m
    for i in range(n):
        task_times[i] = int(sys.stdin.readline())
    for i in range(m):
        quiet_times[i] = int(sys.stdin.readline())
    task_times.sort(reverse=True)
    quiet_times.sort(reverse=True)
    # print(task_times)
    # print(quiet_times)
    i = 0
    j = 0
    while i < n and j < m: 
        if quiet_times[j] >= task_times[i]:
            i += 1
        j += 1
    print(n - i)

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    main(n, m)
