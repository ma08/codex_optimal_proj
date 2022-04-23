
def solution(A):
    num_of_cars = 0
    for i in range(len(A) - 1, -1, -1):
        if A[i] == 0:
            num_of_cars += 1
        else:
            num_of_cars -= 1
            if num_of_cars < 0:
                return 0
    return 1
