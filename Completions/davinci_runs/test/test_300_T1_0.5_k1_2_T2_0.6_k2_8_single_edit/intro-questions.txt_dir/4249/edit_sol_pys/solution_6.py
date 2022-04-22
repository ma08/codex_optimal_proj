n, m = map(int, input().split())


a = list(map(int, input().split()))
b = list(map(int, input().split()))

def get_min_days(a, b, m):
    if a[0] + b[0] >= m:
        return 0
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
