

def is_arithmetic_progression(arr, n):
    return n == 1 or len(set([arr[i+1] - arr[i] for i in range(n-1)])) == 1

def min_changes(arr, n):
    if n == 2:
        return 0
    if n == 3:
        return -1

    if is_arithmetic_progression(arr, n):
        return 0
    else:
        return 1

if __name__ == "__main__":
    n = int(raw_input())
    arr = list(map(int, raw_input().split()))
    print min_changes(arr, n)
