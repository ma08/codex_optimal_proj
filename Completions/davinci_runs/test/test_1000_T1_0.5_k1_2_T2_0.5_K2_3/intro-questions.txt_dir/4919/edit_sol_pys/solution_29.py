
def find_max(l):
    max_val = l[0]
    for i in range(1, len(l)):
        if l[i] > max_val:
            max_val = l[i]
    return max_val


def find_min(l):
    min_val = l[0]
    for i in range(1, len(l)):
        if l[i] < min_val:
            min_val = l[i]
    return min_val


def find_avg(l):
    sum_val = 0
    for i in range(len(l)):
        sum_val += l[i]
    return sum_val / len(l)


def find_sum(l):
    sum_val = 0
    for i in range(len(l)):
        sum_val += l[i]
    return sum_val


def find_median(l):
    copy = sorted(l)
    if len(copy) % 2 == 0:
        median = (copy[len(copy) // 2] + copy[(len(copy) // 2) - 1]) / 2
    else:
        median = copy[len(copy) // 2]
    return median


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(find_max(l))
    print(find_min(l))
    print(find_avg(l))
    print(find_sum(l))
    print(find_median(l))
