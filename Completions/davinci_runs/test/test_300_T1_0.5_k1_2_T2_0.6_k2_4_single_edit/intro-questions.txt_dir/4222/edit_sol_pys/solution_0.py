

import sys

def main():
    n = int(sys.stdin.readline())
    arr = sorted(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    for _ in range(m):
        print(binary_search(arr, int(sys.stdin.readline())))

def binary_search(arr, target):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return 0

if __name__ == '__main__':
    main()
