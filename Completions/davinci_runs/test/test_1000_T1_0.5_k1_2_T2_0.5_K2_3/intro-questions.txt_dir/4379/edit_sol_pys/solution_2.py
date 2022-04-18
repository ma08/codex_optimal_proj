
def find_longest_increasing_subsequence(arr):
    pass

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    max_len, max_indices = find_longest_increasing_subsequence(arr)
    print(max_len)
    print(" ".join(map(str, max_indices)))
