

N = int(input())
A = list(map(int, input().split()))

def bubbleSort(A):
    for i in range(N-1):
        for j in range(N-1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                print(*A)

bubbleSort(A)

print(*A)
