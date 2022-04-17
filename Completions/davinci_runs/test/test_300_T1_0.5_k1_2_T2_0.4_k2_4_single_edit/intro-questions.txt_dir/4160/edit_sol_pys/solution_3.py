

n = int(input())
a = [int(i) for i in input().split()]


def get_max_index(a):
    max_i = 0
    for i in range(1, len(a)):
        if a[i] > a[max_i]:
            max_i = i
    return max_i


def get_max_index_2(a):
    max_i = 0
    for i in range(1, len(a)):
        if a[i] > a[max_i]:
            max_i = i
    return max_i


def get_min_index(a):
    min_i = 0
    for i in range(1, len(a)):
        if a[i] < a[min_i]:
            min_i = i
    return min_i


def get_min_index_2(a):
    min_i = 0
    for i in range(1, len(a)):
        if a[i] < a[min_i]:
            min_i = i
    return min_i


def get_max(a):
    return a[get_max_index(a)]


def get_min(a):
    return a[get_min_index(a)]


def get_max_2(a):
    return a[get_max_index_2(a)]


def get_min_2(a):
    return a[get_min_index_2(a)]


max_i = get_max_index(a)
min_i = get_min_index(a)

if max_i < min_i:
    max_i, min_i = min_i, max_i

if max_i == min_i:
    max_i = get_max_index_2(a)
    min_i = get_min_index_2(a)
    if max_i < min_i:
        max_i, min_i = min_i, max_i

print(max_i, min_i)
