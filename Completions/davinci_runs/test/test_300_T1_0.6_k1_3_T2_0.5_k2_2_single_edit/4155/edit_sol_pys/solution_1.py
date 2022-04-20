import sys
input = sys.stdin.readline


N = int(input().rstrip())
A = list(map(int, input().split()))

def selection_sort(A):
    n = len(A)
    count = 0
    for i in range(n-1):
        minj = i
        for j in range(i, n):
            if A[j] < A[minj]:
                minj = j
        if i != minj:
            A[i], A[minj] = A[minj], A[i]
            count += 1
    return count

count = selection_sort(A)
print(' '.join(map(str, A)))
print(count) 
