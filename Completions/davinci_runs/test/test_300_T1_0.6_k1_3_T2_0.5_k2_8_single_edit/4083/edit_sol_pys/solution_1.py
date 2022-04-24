
import math


def get_answer(n, k, array):
    answer = 0
    min_element = min(array) - 1
    for element in array:
        answer += math.ceil(element / min_element)
    return answer


if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]
    array = [int(x) for x in input().split()]
    print(get_answer(n, k, array))
