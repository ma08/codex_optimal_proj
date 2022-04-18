



def solution(n, array):
    if n == 2:
        if abs(array[0] - array[1]) == 1 or (array[0] % 2 == array[1] % 2):
            return True
        else:
            return False
    else:
        if array[0] % 2 == array[1] % 2:
            return solution(n - 2, array[2:])
        elif abs(array[0] - array[1]) == 1:
            return solution(n - 2, array[2:])
        else:
            return solution(n - 2, array[1:])


t = int(input())
for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    if solution(n, array):
        print("YES")
    else:
        print("NO")
