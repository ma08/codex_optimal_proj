

def find_missing(lst):
    lst = sorted(lst)
    for i in range(len(lst)):
        if lst[i] != i:
            return i

print(find_missing([0, 1, 2, 4, 5, 6, 7]))
print(find_missing([1, 2, 3, 4, 6, 7, 8]))
print(find_missing([0, 1, 2, 3, 4, 5, 6, 7, 9]))
