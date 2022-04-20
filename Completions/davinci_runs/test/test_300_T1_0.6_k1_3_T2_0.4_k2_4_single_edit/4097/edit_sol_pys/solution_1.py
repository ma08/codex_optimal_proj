

def is_arithmetic_progression(arr):
    return len(set(arr)) == 1 or len(set([arr[i+1] - arr[i] for i in range(len(arr) - 1)])) == 1

def min_changes(arr):
    if is_arithmetic_progression(arr):
        return -1
    else:
        return 1

if __name__ == "__main__":
    n = int(raw_input())
    arr = list(map(int, raw_input().split()))
    print(min_changes(arr))
