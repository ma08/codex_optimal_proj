import math

def count_digits(n):
    digits = 0
    while n > 0:
        n = n // 10
        digits += 1
    return digits

def find_digit(n):
    if n == 1:
        return 1
    digits = count_digits(n)
    group_length = 9 * 10 ** (digits - 1) * digits
    groups = math.ceil(n / group_length)
    group_number = n % group_length
    if group_number == 0:
        group_number = group_length
    num = group_number - 1
    num_in_group = math.ceil(num / digits)
    num_in_group_position = num % digits
    if num_in_group_position == 0:
        num_in_group_position = digits
    return int(str(num_in_group)[num_in_group_position - 1])

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n = int(input())
        print(find_digit(n))
