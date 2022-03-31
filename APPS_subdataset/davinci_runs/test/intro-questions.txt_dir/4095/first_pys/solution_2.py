


def read_list_int():
    return list(map(int, input().split(' ')))


def read_single_int():
    return int(input())


def get_number_of_pairs(n, m, p):
    temp_list = []
    for index in range(n):
        temp_list.append(index)
    temp_list.sort(key=lambda i: p[i])
    median_index = n // 2
    median = temp_list[median_index]
    if n % 2 == 0:
        median_2 = temp_list[median_index - 1]
    else:
        median_2 = median
    result = 0
    # print(median, median_2)
    # print(temp_list)
    for index in range(n):
        if p[index] == median:
            result += temp_list.index(index) + 1
    for index in range(n):
        if p[index] == median_2:
            result += temp_list.index(index) + 1
    return result


if __name__ == '__main__':
    n, m = read_list_int()
    p = read_list_int()
    print(get_number_of_pairs(n, m, p))