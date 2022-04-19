
import math

def main():
    h, n = map(int, input().split())
    arr = list(map(int, input().split()))  # [a, b, c, d]

    if sum(arr) >= 0:  # a + b + c + d >= 0
        print(-1)  # -1
        return  # exit

    # find the max
    max_index, max_value = 0, arr[0]  # max_index = 0, max_value = a
    for i in range(1, n):
        if arr[i] > max_value:  # if b > a
            max_index = i  # max_index = 1
            max_value = arr[i]  # max_value = b

    # find the min
    min_index, min_value = 0, arr[0]  # min_index = 0, min_value = a
    for i in range(1, n):
        if arr[i] < min_value:  # if b < a
            min_index = i  # min_index = 1
            min_value = arr[i]  # min_value = b

    # find the next max
    next_max_index, next_max_value = 0, arr[0]  # next_max_index = 0, next_max_value = a
    for i in range(1, n):
        if arr[i] > next_max_value and i != max_index:  # if c > a and 2 != 1
            next_max_index = i  # next_max_index = 2
            next_max_value = arr[i]  # next_max_value = c

    # find the next min
    next_min_index, next_min_value = 0, arr[0]  # next_min_index = 0, next_min_value = a
    for i in range(1, n):
        if arr[i] < next_min_value and i != min_index:  # if c < a and 2 != 1
            next_min_index = i  # next_min_index = 2
            next_min_value = arr[i]  # next_min_value = c

    # print(max_index, max_value)
    # print(min_index, min_value)
    # print(next_max_index, next_max_value)
    # print(next_min_index, next_min_value)

    if max_value + next_min_value < 0:  # b + c < 0
        print(n)  # 4
        return  # exit

    if min_value + next_max_value > 0:  # b + c > 0
        print(n)  # 4
        return  # exit

    if max_index > min_index:  # 1 > 0
        print(n + min_index + 1)  # 4 + 0 + 1 = 5
        return  # exit

    if min_index > max_index:  # 0 > 1
        print(n + max_index + 1)  # 4 + 1 + 1 = 6
        return  # exit

    print(-1)  # -1
    return  # exit


if __name__ == "__main__":
    main()
