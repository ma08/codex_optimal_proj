import math


def get_answer(n, k, array):
    answer = 0
    min_element = min(array)
    for element in array:
        answer += math.ceil(element / min_element) - 1
    return answer <= k


if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]
    array = [int(x) for x in input().split()]
    if get_answer(n, k, array):
        print("YES")
    else:
        print("NO")
