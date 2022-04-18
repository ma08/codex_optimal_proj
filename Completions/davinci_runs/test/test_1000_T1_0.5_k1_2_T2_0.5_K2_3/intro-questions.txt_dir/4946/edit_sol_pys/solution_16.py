# This is the solution for Time Complexity > PermMissingElem
# This is marked as RESPECTABLE difficulty


def solution(A):
    n = len(A) + 1
    return n * (n + 1) / 2 - sum(A)

if __name__ == '__main__':
    print(solution([2, 3, 1, 5]))
