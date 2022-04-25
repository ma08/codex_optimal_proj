

n, m = map(int, input().split()) # n = number of cups, m = number of pages
cups = list(map(int, input().split())) # list of number of pages written per cup

#sorted_cups = sorted(cups, reverse=False) # sorted list of number of pages written per cup

def get_pages_written(cups, day): # gets the number of pages written on a specific day
    if day == 0:
        return cups[0]
    else:
        return cups[day] - day

def get_pages_written_for_day(cups, day): # gets the number of pages written on a specific day
    pages = 0
    for i in range(day+1):
        pages += get_pages_written(cups, i)
    return pages

def get_pages_written_for_n_days(cups, n): # gets the number of pages written for n days
    pages = 0
    for i in range(n):
        pages += get_pages_written_for_day(cups, i)
    return pages

def get_min_days(cups, m): # gets the minimum number of days to write m pages
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
