

n = int(input())
s = input()

# first half and second half
first_half = s[:n//2] # first half
second_half = s[n//2:] # second half

# count a and b
a_count_first_half = first_half.count('a') # first half
b_count_first_half = first_half.count('b') # first half
a_count_second_half = second_half.count('a') # second half
b_count_second_half = second_half.count('b') # second half

# difference 1 and difference 2
difference = abs(a_count_first_half - b_count_first_half)
difference2 = abs(a_count_second_half - b_count_second_half)

# operations (minimum)
operations = min(difference, difference2)

# output
print(operations)

# modified string
if difference < difference2:
    print(first_half + second_half)
else:
    print(second_half + first_half)
