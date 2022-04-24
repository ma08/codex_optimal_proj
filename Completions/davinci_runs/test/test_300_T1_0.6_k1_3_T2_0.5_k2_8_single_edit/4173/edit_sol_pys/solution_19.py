

import math

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(int(input()))

    for query in queries:
        print(binary_search(arr, query))

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return "YES"
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return "NO"

if __name__ == "__main__":
    main()
