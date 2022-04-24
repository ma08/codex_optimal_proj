
n, k = map(int, input().split())
a = list(map(int, input().split()))

def get_max_number(l):
    return max(l)

def get_max_number_index(l):
    return l.index(get_max_number(l))

def get_min_number(l):
    return min(l)

def get_min_number_index(l):
    return l.index(get_min_number(l))

def get_number(l, i):
    return l[i]

def get_half_number(l, i):
    return l[i] // 2

def is_number_multiple_of_two(l, i):
    return (l[i] & 1) == 0

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
