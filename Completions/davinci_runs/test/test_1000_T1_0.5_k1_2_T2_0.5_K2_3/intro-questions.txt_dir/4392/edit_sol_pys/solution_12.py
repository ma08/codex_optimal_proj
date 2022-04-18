
def is_sorted(array, m):
    s = set()
    for i in range(m):
        s.add(array[i] - 1)
    for i in range(n - 1):
        if i in s:
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    for i in range(n - 1):
        if array[i] > array[i + 1]:
            return False
    return True
