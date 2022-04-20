

def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        print_array(arr)
        print()

n = int(input().strip())
arr = [int(i) for i in input().strip().split()]

insertion_sort(arr)
