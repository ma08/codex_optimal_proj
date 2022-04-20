

def ravioli_sort(n, arr, count):
    if n == 1 or count == 0:
        return count
    for i in range(n-1): 
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            count += 1
    return ravioli_sort(n-1, arr, count)

n = int(input())
arr = list(map(int, input().split()))

print(ravioli_sort(n, arr, 0))
