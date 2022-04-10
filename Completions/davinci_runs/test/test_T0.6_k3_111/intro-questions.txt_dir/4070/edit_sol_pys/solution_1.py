
def solution(n, lost, reserve):
    for i in reserve:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)
    for i in lost:
        if i - 1 in reserve:
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            reserve.remove(i + 1)
    return n - len(lost)



print(solution(5, [2, 4], [1, 3, 5]))
