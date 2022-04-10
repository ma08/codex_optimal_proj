

def solution(n, array, string):
    l = 1
    r = 1
    i = 1
    j = 1
    temp = array[0]
    while i < n:
        if array[i] > temp:
            l += 1
            temp = array[i]
            string += 'L'
        i += 1
    temp = array[n-1]
    while j < n:
        if array[n-1-j] < temp:
            r += 1
            temp = array[n-1-j]
            string += 'R'
        j += 1
    if l > r:
        return l
    else:
        return r


n = int(input())
array = [int(x) for x in input().split()]

print(solution(n, array, 'L'))
print(solution(n, array, 'R'))
