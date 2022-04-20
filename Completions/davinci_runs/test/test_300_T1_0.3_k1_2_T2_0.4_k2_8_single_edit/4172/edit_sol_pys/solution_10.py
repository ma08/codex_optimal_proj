
def min_moves(arr, k):
    arr.sort()
    return max(0, arr[-1] - arr[0] - 2 * k)


if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(min_moves(arr, k))
