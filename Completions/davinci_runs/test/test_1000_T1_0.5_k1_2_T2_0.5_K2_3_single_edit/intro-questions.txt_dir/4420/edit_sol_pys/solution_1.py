

# cook your dish here
t = int(input())
for _ in range(t):
    x, y, n = map(int, input().split())


def bin_search(arr, low, high, x):
    if high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return bin_search(arr, low, mid - 1, x)
        else:
            return bin_search(arr, mid + 1, high, x)
    else:
        return -1
    print(n - (n % x) + y)
