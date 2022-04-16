

n, k = map(int, input().split())
days = list(map(int, input().split()))

#sorted_days = sorted(days, reverse=True)

def get_pages_written(days, day):
    if day == 0:
        return days[0]
    else:
        return days[day] - day

def get_pages_written_for_day(days, day):
    pages = 0
    for i in range(day+1):
        pages += get_pages_written(days, i)
    return pages

def get_pages_written_for_n_days(days, n):
    pages = 0
    for i in range(n):
        pages += get_pages_written_for_day(days, i)
    return pages

def get_min_days(days, k):
    if get_pages_written_for_n_days(days, 1) >= k:
        return 1
    left = 1
    right = n
    while left < right:
        mid = (left + right) // 2
        if get_pages_written_for_n_days(days, mid) >= k:
            right = mid
        else:
            left = mid + 1
    if get_pages_written_for_n_days(days, left) >= k:
        return left
    else:
        return -1

print(get_min_days(days, k))
