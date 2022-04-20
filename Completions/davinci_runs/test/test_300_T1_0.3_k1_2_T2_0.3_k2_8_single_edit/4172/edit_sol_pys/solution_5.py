
def min_moves(arr, k):
    arr.sort()
    min_val = arr[0]  # min value
    max_val = arr[-1]  # max value
    if max_val - min_val >= k:  # if difference between max and min is greater than k
        return -1
    else:
        return max_val - min_val  # return the difference


if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(min_moves(arr, k))
