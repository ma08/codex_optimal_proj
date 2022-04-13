# This is the solution for Counting Elements > PermCheck
#
# This is marked as RESPECTABLE difficulty


def solution(A):
    n = len(A)
    count = [False] * (n + 1)
    for i in range(n):
        if A[i] > n:
            return 0
        if count[A[i]]:
            return 0
        count[A[i]] = True
    return 1

if __name__ == '__main__':
    print(solution([4, 1, 3, 2]))
