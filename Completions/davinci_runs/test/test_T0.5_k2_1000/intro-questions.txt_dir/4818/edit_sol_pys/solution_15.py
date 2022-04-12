
def main():
    n, m = map(int, input().split())
    tasks = list(map(int, input().split()))
    intervals = list(map(int, input().split()))
    tasks.sort()

    intervals.sort()

    result = 0
    task_index = 0
    interval_index = 0
    while task_index < n and interval_index < m:
        if tasks[task_index] <= intervals[interval_index]:
            result += 1
            task_index += 1
        interval_index += 1
    print(result)


if __name__ == '__main__':
    main()
