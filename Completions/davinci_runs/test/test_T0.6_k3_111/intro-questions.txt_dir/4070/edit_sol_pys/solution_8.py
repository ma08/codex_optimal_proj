# input

n = int(input())
# function

def solution(x):
    i = 1
    j = 1
    while i < x:
        i += j
        j += 1
    if i == x and (j % 2 == 1):
        return 1
    else:
        return 0
# output

print(solution(n))
