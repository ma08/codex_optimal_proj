# import sys
# sys.stdin = open('input.txt', 'r')


# def is_possible(n, m):
#     if n == 1 or m == 1:
#         return True
#     if n % 2 == 0 and m % 2 == 0:
#         return True
#     return False

# for _ in range(int(input())):
#     n, m = [int(x) for x in input().split()]
#     if is_possible(n, m):
#         print('YES')
#     else:
#         print('NO')


def is_possible(arr):
    for i in range(len(arr) - 1):
        if arr[i] == arr[i+1]:
            return False
    return True


def solve(arr, index):
    if index == len(arr):
        if is_possible(arr):
            return 1
        return 0

    cnt = 0
    for i in range(1, 4):
        arr[index] = i
        cnt += solve(arr, index + 1)
    return cnt


print(solve([0] * int(input()), 0))
