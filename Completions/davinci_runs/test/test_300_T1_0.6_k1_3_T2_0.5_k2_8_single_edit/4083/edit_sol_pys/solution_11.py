
import math


def get_answer(n, k, array_):
    answer = 0
    min_element = min(array_)
    for element in array_:
        answer += math.ceil(element / min_element) - 1
    return answer


if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]
    array_ = [int(x) for x in input().split()]
    print(get_answer(n, k, array_))
