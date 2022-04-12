

def solution(A):
    A.sort()
    for i in range(len(A)):
        if A[i] != i + 1:
            return 0
    return 1

print(solution([4, 1, 3, 2]))
