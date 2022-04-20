
n, k = map(int, input().split())
a = list(map(int, input().split()))

def get_max_number():
    return max(a) 

def get_max_number_index():
    return a.index(get_max_number())

def get_min_number():
    return min(a) 

def get_min_number_index():
    return a.index(get_min_number()) 

def get_number(i):
    return a[i] 

def get_half_number(i):
    return a[i] // 2 

def is_number_multiple_of_two(i):
    return (a[i] & 1) == 0 

def set_number(i, number):
    a[i] = number

def is_number_same_as_others():
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
