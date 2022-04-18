


def solution(array):
    array.sort()
    for i in range(len(array) - 1):
        if abs(array[i] - array[i + 1]) == 1 or (array[i] % 2 == array[i + 1] % 2 == 0):
            continue
        return False
    return True


t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    if solution(array):
        print("YES")
    else:
        print("NO")
