

n, k = map(int, input().split())
a = list(map(int, input().split()))

def get_max_number(a):
    return max(a)

def get_max_number_index(a):
    return a.index(get_max_number(a))

def get_min_number(a):
    return min(a)

def get_min_number_index(a):
    return a.index(get_min_number(a))

def get_number_at_index(a, i):
    return a[i]

def get_half_number_at_index(a, i):
    return a[i] // 2

def is_number_at_index_multiple_of_two(a, i):
    return (a[i] & 1) == 0

def set_number_at_index(a, i, number):
    a[i] = number

def is_number_same_as_others(a):
    return len(set(a)) == 1

def get_number_of_operations(n, k, a):
    operations = 0

    while not is_number_same_as_others(a):
        if is_number_at_index_multiple_of_two(a, get_max_number_index(a)):
            set_number_at_index(a, get_max_number_index(a), get_half_number_at_index(a, get_max_number_index(a)))
            operations += 1
        else:
            set_number_at_index(a, get_min_number_index(a), get_half_number_at_index(a, get_min_number_index(a)))
            operations += 1

    return operations

print(get_number_of_operations(n, k, a))
