
def min_max(a, n):
    min_val = a[0]
    max_val = a[0]
    for i in range(1, n):
        if a[i] < min_val:
            min_val = a[i]
        if a[i] > max_val:
            max_val = a[i]
    return min_val, max_val


a = [1, 2, 3, 4, 5, 6]
n = len(a)
print(min_max(a, n))
