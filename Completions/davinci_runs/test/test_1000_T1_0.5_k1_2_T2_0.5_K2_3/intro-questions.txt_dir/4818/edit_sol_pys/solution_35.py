
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    tasks = sorted(map(int, sys.stdin.readline().split()), reverse=True)
    free_times = sorted(map(int, sys.stdin.readline().split()), reverse=True)

    task_index = 0
    free_time_index = 0
    completed = 0
    while task_index < n and free_time_index < m:
        if tasks[task_index] <= free_times[free_time_index]:
            task_index += 1
            free_time_index += 1
            completed += 1
        else:
            free_time_index += 1
    print(completed)


if __name__ == '__main__':
    main()
