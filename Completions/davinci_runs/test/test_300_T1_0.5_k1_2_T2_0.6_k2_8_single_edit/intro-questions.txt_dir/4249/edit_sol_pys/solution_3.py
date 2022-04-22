# Example:
# input:
# 3 3
# 5 7 9
# output:
# 2

n, m = map(int, input().split())
cups = list(map(int, input().split()))

def get_pages_written(cups, day):
    if day == 0:
        return cups[0]
    else:
        return cups[day] - day

def get_pages_written_for_day(cups, day):
    pages = 0
    for i in range(day+1):
        pages += get_pages_written(cups, i)
    return pages

def get_pages_written_for_n_days(cups, n):
    pages = 0
    for i in range(n):
        pages += get_pages_written_for_day(cups, i)
    return pages

def get_min_days(cups, m):
    if get_pages_written_for_n_days(cups, 1) >= m:
        return 1
    left = 1
    right = n
    while left < right:
        mid = (left + right) // 2
        if get_pages_written_for_n_days(cups, mid) >= m:
            right = mid
        else:
            left = mid + 1
    if get_pages_written_for_n_days(cups, left) >= m:
        return left
    else:
        return -1

print(get_min_days(cups, m))
