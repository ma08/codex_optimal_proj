
N = int(input())
A = [int(input()) for i in range(N)]

A.sort()

# for i in range(N):
#     print(A[i])

# for i in range(N):
#     print(A[i])


def binary_search(A, key):
    left = 0
    right = len(A)

    while left < right:
        mid = (left + right) // 2
        if A[mid] == key:
            return 1
        elif A[mid] < key:
            left = mid + 1
        else:
            right = mid

    return 0


# for i in range(N):
#     print(binary_search(A, A[i]))


Q = int(input())
T = [int(input()) for i in range(Q)]

for i in range(Q):
    print(binary_search(A, T[i]))
