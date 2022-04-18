def solution(array):
    for i in range(len(array) - 1):
        if array[i] % 2 != array[i + 1] % 2 and abs(array[i] - array[i + 1]) != 1:
            return False
    return True


t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    if solution(n, array):
        print("YES")
    else:
        print("NO")
