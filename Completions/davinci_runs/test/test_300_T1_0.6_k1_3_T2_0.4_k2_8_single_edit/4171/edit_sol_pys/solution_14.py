

n, k = map(int, input().split())
a = list(map(int, input().split()))

def get_max_number(array):
    return max(array)

def get_max_number_index(array):
    return array.index(get_max_number(array))

def get_min_number(array):
    return min(array)

def get_min_number_index(a):
    return a.index(get_min_number(a))

def get_number(a, i):
    return a[i]

def get_half_number(a, i):
    return a[i] // 2

def is_number_multiple_of_two(a, i):
    return (a[i] & 1) == 0

def set_number(a, i, number):
    a[i] = number

def is_number_same_as_others(a):
    return len(set(a)) == 1

def get_number_of_operations(n, k, a):
    operations = 0

    while not is_number_same_as_others(a):
        if is_number_multiple_of_two(a, get_max_number_index(a)):
            a[get_max_number_index(a)] = get_half_number(a, get_max_number_index(a))
            operations += 1
        else:
            a[get_min_number_index(a)] = get_half_number(a, get_min_number_index(a))
            operations += 1

    return operations

print(get_number_of_operations(n, k, a))
