
import math


def get_answer(n, k, array, new_array):
    for i in range(n):
        new_array.append(array[i])
        for j in range(i, n):
            if array[i] < array[j]:
                new_array.append(array[j])
            else:
                new_array.append(array[i])
    return new_array


if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]
    array = [int(x) for x in input().split()]
    new_array = []
    print(get_answer(n, k, array, new_array))
