

def caffeine_dosage(arr, m):
    n = len(arr)
    days = 0
    pages_written = 0
    while pages_written < m and days < n:
        pages_written += arr[days]
        for i in range(1, n):
            if days - i >= 0:
                pages_written += max(0, arr[days - i] - i)
        days += 1
    if pages_written < m:
        return -1
    return days

n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(caffeine_dosage(arr, m))