
def solution(n):
    a = list(map(int, str(n)))
    for i in range(len(a)):
        if a[i] == 0:
            a[i] = 1
        else:
            a[i] = 0
    return int(''.join(map(str, a)))
