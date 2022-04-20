
n, k = map(int, input().split())
a = list(map(int, input().split()))

def get_max_number(numbers):
    return max(numbers)

def get_max_number_index(numbers):
    return numbers.index(get_max_number(numbers))

def get_min_number(numbers):
    return min(numbers)

def get_min_number_index(numbers):
    return numbers.index(get_min_number(numbers))

def get_number(numbers, index):
    return numbers[index]

def get_half_number(numbers, index):
    return numbers[index] // 2

def is_number_multiple_of_two(numbers, index):
    return (numbers[index] & 1) == 0

def set_number(numbers, index, number):
    numbers[index] = number

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
