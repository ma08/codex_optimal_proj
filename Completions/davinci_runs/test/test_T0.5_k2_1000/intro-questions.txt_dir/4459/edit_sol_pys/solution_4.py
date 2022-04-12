
n, k = map(int, input().split())
a = list(map(int, input().split()))[:n]

a.sort()

def binary_search(a, x):
    left = 0
    right = len(a)

    while left < right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid
    return -1


print(binary_search(a, k))
