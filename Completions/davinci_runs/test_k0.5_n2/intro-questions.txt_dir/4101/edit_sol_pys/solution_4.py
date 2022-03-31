#!/usr/bin/env python3

n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

def inverse(arr):
    return [1 - x for x in arr]

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True

def is_sorted_matrix(matrix):
    arr = []
    for i in range(n):
        for j in range(m):
            arr.append(matrix[i][j])
    return is_sorted(arr)

def is_sorted_matrix_inv(matrix):
    for i in range(n):
        if not is_sorted(matrix[i]):
            return False
    for j in range(m):
        arr = []
        for i in range(n):
            arr.append(matrix[i][j])
        if not is_sorted(arr):
            return False
    return True

r = [0] * n
c = [0] * m
for i in range(n):
    if not is_sorted(matrix[i]):
        r[i] = 1
        matrix[i] = inverse(matrix[i])
for j in range(m):
    arr = []
    for i in range(n):
        arr.append(matrix[i][j])
    if not is_sorted(arr):
        c[j] = 1
        for i in range(n):
            matrix[i][j] = 1 - matrix[i][j]

if is_sorted_matrix_inv(matrix, n, m):
    print("YES")
    print("".join(map(str, r)))
    print("".join(map(str, c)))
else:
    print("NO")
