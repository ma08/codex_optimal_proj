

import math

def median(array):
    array.sort()
    if len(array) % 2 == 0:
        return (array[len(array) // 2 - 1] + array[len(array) // 2]) / 2
    else:
        return array[len(array) // 2]

def get_median(array, l, r):
    return median(array[l-1:r])

def get_median_count(array, m):
    count = 0
    for i in range(1, len(array) + 1):
        for j in range(i, len(array) + 1):
            if get_median(array, i, j) == m:
                count += 1
    return count

def main():
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    print(get_median_count(array, m))

if __name__ == "__main__":
    main()