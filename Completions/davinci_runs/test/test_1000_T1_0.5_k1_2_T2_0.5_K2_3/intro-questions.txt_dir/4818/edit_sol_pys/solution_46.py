import sys


def main():
    n, m = map(int, input().split())
    tasks = list(map(int, input().split()))
    intervals = list(map(int, input().split()))
    tasks.sort()
    intervals.sort()

    best = 0
    i = 0
    j = 0
    while i < n and j < m:  # пока не прошли по всем интервалам и задачам
        if tasks[i] <= intervals[j]:
            best += 1
            i += 1
        j += 1
    print(best)  # выводим количество задач, которые можно выполнить


if __name__ == '__main__':
    main()
