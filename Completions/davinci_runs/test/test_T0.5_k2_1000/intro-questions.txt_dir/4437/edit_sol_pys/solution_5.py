

n = int(input())
s = input()

# first half of the string
first_half_of_the_string = s[:n//2]
a_count_first_half_of_the_string = first_half_of_the_string.count('a')
b_count_first_half_of_the_string = first_half_of_the_string.count('b')

# second half of the string
second_half_of_the_string = s[n//2:]
a_count_second_half_of_the_string = second_half_of_the_string.count('a')
b_count_second_half_of_the_string = second_half_of_the_string.count('b')

# difference
difference2 = abs(a_count_second_half_of_the_string - b_count_second_half_of_the_string)

# operations
operations = min(difference, difference2) + abs(a_count_first_half_of_the_string - b_count_first_half_of_the_string)

# output
print(operations)

# modified string
if difference < difference2:
    print(first_half_of_the_string + second_half_of_the_string)
else:
    print(second_half_of_the_string + first_half_of_the_string)
