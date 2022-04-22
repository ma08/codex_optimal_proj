

def bsearch(arr, t):
    l = 0
    r = len(arr) -1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def merge(arr1, arr2):
    i = 0
    j = 0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    res += arr1[i:]
    res += arr2[j:]
    return res


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    arr = merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
