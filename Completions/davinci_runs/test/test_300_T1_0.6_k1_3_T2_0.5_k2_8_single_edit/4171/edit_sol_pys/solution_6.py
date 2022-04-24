
n, k = map(int, input().split())
a = list(map(int, input().split()))

def get_max_number(number_list):
    return max(number_list)

def get_max_number_index(number_list):
    return number_list.index(get_max_number(number_list))

def get_min_number(number_list):
    return min(number_list)

def get_min_number_index(number_list):
    return number_list.index(get_min_number(number_list))

def get_number(number_list, index):
    return number_list[index]

def get_half_number(number_list, index):
    return number_list[index] // 2

def is_number_multiple_of_two(number_list, index):
    return (number_list[index] & 1) == 0

def set_number(number_list, index, number):
    number_list[index] = number

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
