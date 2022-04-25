
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
    group_size = 9 * 10 ** (digits - 1) * digits
    # print(group_size)
    groups = math.ceil(n / group_size)
    # print(groups)
    group_num = n % (group_size + 1)
    if group_num == 0:
        group_num = group_size + 1
    # print(group_num)
    num = group_num
    # print(num)
    num_in_group = math.ceil(num / digits)
    # print(num_in_group)
    num_in_group_pos = num % (digits + 1)
    if num_in_group_pos == 0:
        num_in_group_pos = digits + 1
    # print(num_in_group_pos)
    return int(str(num_in_group)[num_in_group_pos - 1])

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n = int(input())
        print(find_digit(n))
