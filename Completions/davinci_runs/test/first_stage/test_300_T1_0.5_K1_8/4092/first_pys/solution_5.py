
n = int(input())
a = list(map(int, input().split(' ')))

def get_sum(l, r):
    return sum(a[l:r])

def get_sum_to(i):
    return sum(a[:i+1])

def get_sum_from(i):
    return sum(a[i:])

def get_sum_from_to(l, r):
    return sum(a[l:r])

def get_index_of_first_zero_sum_subsegment(l, r):
    if l >= r:
        return None
    if l == r - 1:
        return None
    if get_sum(l, r) == 0:
        return (l, r)
    else:
        mid = (l + r) // 2
        left = get_index_of_first_zero_sum_subsegment(l, mid)
        right = get_index_of_first_zero_sum_subsegment(mid, r)
        if left is not None:
            return left
        elif right is not None:
            return right
        else:
            return None

def get_index_of_last_zero_sum_subsegment(l, r):
    if l >= r:
        return None
    if l == r - 1:
        return None
    if get_sum(l, r) == 0:
        return (l, r)
    else:
        mid = (l + r) // 2
        left = get_index_of_last_zero_sum_subsegment(l, mid)
        right = get_index_of_last_zero_sum_subsegment(mid, r)
        if right is not None:
            return right
        elif left is not None:
            return left
        else:
            return None

def get_index_of_first_zero_sum_subsegment_to(i):
    return get_index_of_first_zero_sum_subsegment(0, i+1)

def get_index_of_last_zero_sum_subsegment_from(i):
    return get_index_of_last_zero_sum_subsegment(i, n)

def get_index_of_first_zero_sum_subsegment_from_to(l, r):
    return get_index_of_first_zero_sum_subsegment(l, r)

def get_index_of_last_zero_sum_subsegment_from_to(l, r):
    return get_index_of_last_zero_sum_subsegment(l, r)

def get_result(i):
    if get_sum_to(i) == 0:
        return get_result(i-1)
    if get_sum_from(i) == 0:
        return get_result(i+1)
    return i

def get_result_from_to(l, r):
    if get_sum_from_to(l, r) == 0:
        a = get_index_of_first_zero_sum_subsegment_from_to(l, r)
        b = get_index_of_last_zero_sum_subsegment_from_to(l, r)
        if a is None or b is None:
            return None
        if a[0] == 0 and b[1] == n:
            return 0
        else:
            return 1 + get_result_from_to(a[0], b[1])
    else:
        return 0


result = get_result_from_to(0, n)

print(result)