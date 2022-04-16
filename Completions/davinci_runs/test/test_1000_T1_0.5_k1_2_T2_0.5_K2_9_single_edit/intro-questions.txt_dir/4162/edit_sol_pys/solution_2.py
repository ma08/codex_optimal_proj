

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binarySearch(arr, 1))

def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    main()
