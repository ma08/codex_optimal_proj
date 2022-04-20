
def min_moves(arr, k):
    return -1 if (max(arr) - min(arr)) >= k else max(arr) - min(arr)

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(min_moves(arr, k))
