

def ravioli_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [1, 2, 3, 4, 5, 6]

print(ravioli_sort(arr))
