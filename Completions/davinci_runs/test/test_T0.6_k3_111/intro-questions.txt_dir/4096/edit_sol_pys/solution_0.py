def cup_of_coffee(n, m, a):
    total_pages = 0
    for i in range(n):
        total_pages += max(0, a[i] - i)

    if total_pages < m:
        return -1

    max_cups = 0
    for i in range(n):
        max_cups += min(a[i], n - i)

    return max_cups


print(cup_of_coffee(3, 2, [1, 2, 3]))
