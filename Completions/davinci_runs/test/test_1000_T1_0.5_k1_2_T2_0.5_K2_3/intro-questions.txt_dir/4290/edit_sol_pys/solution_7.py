

def sum_even_numbers(first_number, second_number):
    return first_number * second_number

first_number, second_number = [int(x) for x in input().split()]
print(sum_even_numbers(first_number, second_number))
