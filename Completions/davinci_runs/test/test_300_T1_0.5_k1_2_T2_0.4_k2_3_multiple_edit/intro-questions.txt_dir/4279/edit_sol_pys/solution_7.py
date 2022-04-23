
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
    # print(digits)
    group_length = 9 * 10 ** (digits - 1) * digits
    # print(group_length)
    groups = math.ceil(n / group_length)
    # print(groups) # 1
    group_number = n % group_length if n % group_length != 0 else group_length
    # print(group_number)
    num = group_number - 1
    # print(num)
    num_in_group = math.ceil(num / digits)
    # print(num_in_group)
    num_in_group_position = num % digits if num % digits != 0 else digits
    # print(num_in_group_position)
    return int(str(num_in_group)[num_in_group_position - 1])

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n = int(input())
        print(find_digit(n))
