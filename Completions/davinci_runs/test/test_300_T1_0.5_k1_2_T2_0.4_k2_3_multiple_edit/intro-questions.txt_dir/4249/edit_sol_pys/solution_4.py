

n, m = map(int, input().split())
cups = list(map(int, input().split()))

# sorted_cups = sorted(cups, reverse=True)

def get_pages_written_for_day(cups, day, n):
    if day == 0:
        return cups[0] if day < n else 0
    else:
        return cups[day] - day if day < n else 0

def get_pages_written_for_n_days(cups, day, n):
    pages = 0
    for i in range(day+1):
        pages += get_pages_written_for_day(cups, i, n)
    return pages

def get_pages_written_for_m_days(cups, n, m):
    pages = 0
    for i in range(n):
        pages += get_pages_written_for_day(cups, i, n)
    return pages

def get_min_days(cups, m):
    if get_pages_written_for_m_days(cups, 1, n) >= m:
        return 1
    left = 1
    right = n
    while left < right:
        mid = (left + right) // 2
        if get_pages_written_for_m_days(cups, mid, n) >= m:
            right = mid
        else:
            left = mid + 1
    if get_pages_written_for_m_days(cups, left) >= m:
        return left
    else:
        return -1

print(get_min_days(cups, m))
