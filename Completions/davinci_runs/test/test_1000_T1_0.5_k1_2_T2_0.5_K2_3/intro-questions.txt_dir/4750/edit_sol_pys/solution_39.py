

from operator import itemgetter

def mergeSort(arr, n):
    if n == 1:
        return arr
    mid = n//2
    left = mergeSort(arr[:mid], mid)
    right = mergeSort(arr[mid:], n - mid)
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    arr = mergeSort(arr, n)
    for i in range(n):
        print(arr[i][0], arr[i][1])

main()
