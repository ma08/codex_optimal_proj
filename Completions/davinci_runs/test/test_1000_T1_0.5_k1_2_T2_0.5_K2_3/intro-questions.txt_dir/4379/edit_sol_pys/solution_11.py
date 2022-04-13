
def is_increasing(arr):
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            return False
    return True

def find_increasing_sub_sequence(arr):
    max_len = 0
    max_indices = None
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if is_increasing(arr[i:j + 1]) and len(arr[i:j + 1]) > max_len:
                max_len = len(arr[i:j + 1])
                max_indices = [i + 1, j + 1]
    return max_len, max_indices


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    max_len, max_indices = find_increasing_sub_sequence(arr)
    print(max_len)
    print(" ".join(map(str, max_indices)))
