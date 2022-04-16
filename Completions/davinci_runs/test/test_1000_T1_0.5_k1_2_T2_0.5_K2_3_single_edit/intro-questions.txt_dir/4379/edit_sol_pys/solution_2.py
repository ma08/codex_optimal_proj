
def is_increasing(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True


def find_increasing_subsequence(arr):
    max_len = 0
    max_indices = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sub_arr = arr[i:j+1]
            if is_increasing(sub_arr) and len(sub_arr) > max_len:
                max_len = len(sub_arr)
                max_indices = sub_arr
    return max_len, max_indices


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    max_len, max_indices = find_increasing_subsequence(arr)
    print(max_len)
    print(" ".join(map(str, max_indices)))
