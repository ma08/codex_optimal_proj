

n = int(input())
s = input()

# first half a
first_half_a = s[:n//2]
a_count_first_half_a = first_half_a.count('a')
b_count_first_half_a = first_half_a.count('b')

# first half b
first_half_b = s[:n//2]
a_count_first_half_b = first_half_b.count('a')
b_count_first_half_b = first_half_b.count('b')

# second half a
second_half_a = s[n//2:]
a_count_second_half_a = second_half_a.count('a')
b_count_second_half_a = second_half_a.count('b')

# second half b
second_half_b = s[n//2:]
a_count_second_half_b = second_half_b.count('a')
b_count_second_half_b = second_half_b.count('b')

# difference
difference_a = abs(a_count_first_half_a - b_count_first_half_a)
difference_b = abs(a_count_first_half_b - b_count_first_half_b)
difference2_a = abs(a_count_second_half_a - b_count_second_half_a)
difference2_b = abs(a_count_second_half_b - b_count_second_half_b)

# operations
operations_a = min(difference_a, difference2_a)
operations_b = min(difference_b, difference2_b)

# output
print(min(operations_a, operations_b))

# modified string
if operations_a < operations_b:
    if difference_a < difference2_a:
        print(first_half_a + second_half_a)
    else:
        print(second_half_a + first_half_a)
else:
    if difference_b < difference2_b:
        print(first_half_b + second_half_b)
    else:
        print(second_half_b + first_half_b)
