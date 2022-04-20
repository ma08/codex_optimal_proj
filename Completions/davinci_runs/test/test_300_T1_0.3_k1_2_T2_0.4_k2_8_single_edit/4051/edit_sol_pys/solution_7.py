

def find_max_subarray(n, arr):
    max_sum = 0
    for i in range(n):
        for j in range(i, n):
            current_sum = 0
            for k in range(i, j+1):
                current_sum += arr[k]
            max_sum = max(max_sum, current_sum)
    return max_sum

n = int(input())
arr = list(map(int, input().strip().split()))

print(find_max_subarray(n, arr))
