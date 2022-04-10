

def solution(n, array):
    l = 1
    r = 1
    i = 1
    j = 1
    temp = array[0]
    string = 'L'
    while i < n:
        if array[i] > temp:
            l += 1
            temp = array[i]
            string += 'L'
        i += 1
    temp = array[n-1]
    string = 'R'
    while j < n:
        if array[n-1-j] < temp:
            r += 1
            temp = array[n-1-j]
            string += 'R'
        j += 1
    if l > r:
        return l, string
    else:
        return r, string[::-1]


n = int(input())
array = [int(x) for x in input().split()]

print(solution(n, array)[0])
print(solution(n, array)[1])
