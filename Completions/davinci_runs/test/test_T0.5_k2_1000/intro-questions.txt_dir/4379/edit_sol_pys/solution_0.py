

def is_increasing(arr):
    for i in range(len(arr)):
        if i == len(arr) - 1:
            return True
        if arr[i] >= arr[i+1]:
            return False 

def find_increasing_subsequence(arr):
    max_len = 1
    max_indices = [1, 1]
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if is_increasing(arr[i:j+1]) and len(arr[i:j+1]) >= max_len:
                max_len = len(arr[i:j+1])
                max_indices = [i+1, j+1]
    return max_len, max_indices


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    max_len, max_indices = find_increasing_subsequence(arr)
    print(max_len)
    print(" ".join(map(str, max_indices)))
