
import sys
sys.setrecursionlimit(1000000)
n, m = map(int, input().split())
cups = list(map(int, input().split()))
sorted_cups = sorted(cups, reverse=True)

def get_pages_written(cups, day):
    if day == 0:
        return cups[0]
    else:
        return cups[day] - day

def get_pages_written_for_day(day):
    pages = 0
    for i in range(day+1):
        pages += get_pages_written(sorted_cups, i)
    return pages

def get_pages_written_for_n_days(n):
    pages = 0
    for i in range(n):
        pages += get_pages_written_for_day(i)
    return pages

def get_min_days(m):
    if get_pages_written_for_n_days(1) >= m:
        return 1
    left = 1
    right = n
    while left < right:
        mid = (left + right) // 2
        if get_pages_written_for_n_days(mid) >= m:
            right = mid
        else:
            left = mid + 1
    if get_pages_written_for_n_days(cups, left) >= m:
        return left
    else:
        return -1

print(get_min_days(cups, m))
