

n = int(input()) # length of string
s = input()

# first half of string, a and b count
first_half = s[:n//2] # first half of string
a_count_first_half = first_half.count('a')
b_count_first_half = first_half.count('b')

# second half of string, a and b count
second_half = s[n//2:] # second half of string
a_count_second_half = second_half.count('a')
b_count_second_half = second_half.count('b')

# difference, first half and second half
difference = abs(a_count_first_half - b_count_first_half)
difference2 = abs(a_count_second_half - b_count_second_half)

# operations, minimum number of operations
operations = min(difference, difference2)

# output, minimum number of operations
print(operations)

# modified string, first half and second half
if difference < difference2:
    print(first_half + second_half)
else:
    print(second_half + first_half)
