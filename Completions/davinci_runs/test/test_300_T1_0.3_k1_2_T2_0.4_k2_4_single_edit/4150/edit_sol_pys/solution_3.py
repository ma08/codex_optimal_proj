
def find_max_index(a):
    max_value = a[0]
    max_index = 0
    for i in range(1, len(a)):
        if a[i] > max_value:
            max_value = a[i]
            max_index = i
    return max_index
