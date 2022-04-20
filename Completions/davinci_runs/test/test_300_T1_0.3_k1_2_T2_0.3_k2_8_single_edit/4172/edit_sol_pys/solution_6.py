
def min_moves(arr, k):
    arr.sort()
    return arr[-1] - arr[0] if arr[-1] - arr[0] < k else -1

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(min_moves(arr, k))
