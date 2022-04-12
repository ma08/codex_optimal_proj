
def solution(A):
    A.sort()
    n = len(A)
    for i in range(n-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1
    return 0
