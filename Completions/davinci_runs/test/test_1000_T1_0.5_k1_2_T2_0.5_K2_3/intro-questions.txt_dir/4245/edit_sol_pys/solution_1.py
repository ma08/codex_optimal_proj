

import sys, math, copy

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

def swap(a, b, lst):
    lst[a], lst[b] = lst[b], lst[a]
    return lst

def bubble_sort(lst):
    for i in range(n):
        for j in range(n-1):
            if lst[j] > lst[j+1]:
                lst = swap(j, j+1, lst)
    return lst

def selection_sort(lst):
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst = swap(i, min_idx, lst)
    return lst

def insertion_sort(lst):
    for i in range(1, n):
        for j in range(i, 0, -1):
            if lst[j] < lst[j-1]:
                lst = swap(j, j-1, lst)
            else:
                break
    return lst

bubble_lst = bubble_sort(copy.deepcopy(lst))
selection_lst = selection_sort(copy.deepcopy(lst))
insertion_lst = insertion_sort(copy.deepcopy(lst))

print(" ".join(map(str, bubble_lst)))
print(" ".join(map(str, selection_lst)))
print(" ".join(map(str, insertion_lst)))
