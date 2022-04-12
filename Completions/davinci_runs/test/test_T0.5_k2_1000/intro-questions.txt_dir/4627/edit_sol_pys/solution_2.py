def solution(n, arr):
    if n == 2 and abs(arr[0] - arr[1]) == 1 or (arr[0] % 2 == arr[1] % 2):
        return True
    elif n == 2 and abs(arr[0] - arr[1]) != 1 and (arr[0] % 2 != arr[1] % 2):
        return False
    elif arr[0] % 2 == arr[1] % 2:
        return solution(n - 2, arr[2:])
    elif abs(arr[0] - arr[1]) == 1:
        return solution(n - 2, arr[2:])
    else:
        return solution(n - 2, arr[1:])


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if solution(n, arr):
        print("YES")
    else:
        print("NO")
