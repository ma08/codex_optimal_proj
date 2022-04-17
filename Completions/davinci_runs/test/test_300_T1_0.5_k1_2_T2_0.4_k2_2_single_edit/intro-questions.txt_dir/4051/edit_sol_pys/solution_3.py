
n = int(input())
arr = list(map(int, input().split()))

def check_ravioli_sort(arr):
    sorted_arr = sorted(arr)
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            return "NO"
    return "YES"


print(check_ravioli_sort(arr))
