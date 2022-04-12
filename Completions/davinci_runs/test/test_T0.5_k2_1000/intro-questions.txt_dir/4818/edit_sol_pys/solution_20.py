import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    tasks = sorted(map(int, sys.stdin.readline().split()))
    free_time = sorted(map(int, sys.stdin.readline().split()))

    task_index = 0
    free_time_ind = 0
    completed = 0
    while task_index < n and free_time_ind < m:
        if tasks[task_index] <= free_time[free_time_ind]:
            task_index += 1
            free_time_ind += 1
            completed += 1
        else:
            free_time_ind += 1
    print(completed)

if __name__ == '__main__':
    main()
