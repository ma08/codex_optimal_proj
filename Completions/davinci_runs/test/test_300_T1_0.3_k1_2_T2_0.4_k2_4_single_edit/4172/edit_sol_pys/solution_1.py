
def min_moves(arr, k):
    arr.sort()
    min_val = arr[0] + k
    max_val = arr[-1] - k
    if min_val > max_val:
        min_val, max_val = max_val, min_val
    diff = max_val - min_val
    return 0 if diff < 0 else diff

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(min_moves(arr, k))
