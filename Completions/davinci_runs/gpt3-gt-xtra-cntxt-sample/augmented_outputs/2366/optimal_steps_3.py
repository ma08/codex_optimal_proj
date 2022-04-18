# Implementation of Merge Sort
def merge_sort(array):

    if len(array) > 1:
        # Dividing the array into two halves
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # Recursively sort the two halves
        merge_sort(left)
        merge_sort(right)

        # Initialize the indices
        i = 0
        j = 0
        k = 0

        # Merge the two halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # Merge the remaining elements in the left half
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        # Merge the remaining elements in the right half
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

# Solution to the problem
def bad_prices(array):
    merge_sort(array)
    min_price = array[0]
    bad_price_count = 0
    for i in range(1, len(array)):
        if array[i] < min_price:
            bad_price_count += 1
        else:
            min_price = array[i]
    return bad_price_count

# Driver code
t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    print(bad_prices(array))