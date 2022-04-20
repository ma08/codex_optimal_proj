import sys

def min_moves(arr, k):
    arr.sort()
    min_val = arr[0]
    max_val = arr[-1]
    if max_val - min_val >= k:
        return -1
    else:
        return max_val - min_val

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    print(min_moves(arr, k))
