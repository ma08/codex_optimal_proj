
import math

def main():
    h, n = map(int, input().split())
    arr = list(map(int, input().split()))

    # if sum(arr) >= 0:
    #     print(-1)
    #     return

    # find the max
    max_index, max_value = 0, arr[0]
    for i in range(1, n):
        if arr[i] > max_value:
            max_index = i
            max_value = arr[i]

    # find the min
    min_index, min_value = 0, arr[0]
    for i in range(1, n):
        if arr[i] < min_value:
            min_index = i
            min_value = arr[i]

    # find the next max
    next_max_index, next_max_value = 0, arr[0]
    for i in range(1, n):
        if arr[i] > next_max_value and i != max_index:
            next_max_index = i
            next_max_value = arr[i]

    # find the next min
    next_min_index, next_min_value = 0, arr[0]
    for i in range(1, n):
        if arr[i] < next_min_value and i != min_index:
            next_min_index = i
            next_min_value = arr[i]

    # print(max_index, max_value)
    # print(min_index, min_value)
    # print(next_max_index, next_max_value)
    # print(next_min_index, next_min_value)

    if max_value + next_min_value < 0:
        print(n)
        return

    if min_value + next_max_value > 0:
        print(n)
        return

    if max_index > min_index:
        print(n + min_index + 1)
        return

    if min_index > max_index:
        print(n + max_index + 1)
        return

    print(-1)
    return


if __name__ == "__main__":
    main()
