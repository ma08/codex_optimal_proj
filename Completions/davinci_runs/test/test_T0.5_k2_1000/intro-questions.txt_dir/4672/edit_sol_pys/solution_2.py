#!/usr/bin/env python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
    return arr


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    size = max_val - min_val + 1
    count = [0] * size

    for i in range(len(arr)):
        count[arr[i] - min_val] += 1

    j = 0
    for i in range(size):
        for k in range(count[i]):
            arr[j] = i + min_val
            j += 1
    return arr


def radix_sort(arr):
    max_val = max(arr)

    exp = 1
    while max_val//exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr


def counting_sort(arr, exp):
    size = len(arr)
    output = [0] * size
    count = [0] * 10

    for i in range(size):
        index = arr[i]//exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = size - 1
    while i >= 0:
        index = arr[i]//exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(size):
        arr[i] = output[i]


print(bubble_sort(arr))
print(insertion_sort(arr))
print(selection_sort(arr))
print(merge_sort(arr))
print(quick_sort(arr, 0, len(arr)-1))
print(heap_sort(arr))
print(counting_sort(arr))
print(radix_sort(arr))
