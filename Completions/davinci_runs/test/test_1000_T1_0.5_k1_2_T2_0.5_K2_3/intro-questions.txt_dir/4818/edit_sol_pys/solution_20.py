
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    task_times = list(map(int, sys.stdin.readline().split()))
    quiet_times = list(map(int, sys.stdin.readline().split()))
    task_times.sort()
    quiet_times.sort()
    i = j = 0
    count = 0
    while i < n and j < m:
        if task_times[i] <= quiet_times[j]:
            count += 1
            i += 1
        j += 1
    print(count)

if __name__ == "__main__":
    main()
