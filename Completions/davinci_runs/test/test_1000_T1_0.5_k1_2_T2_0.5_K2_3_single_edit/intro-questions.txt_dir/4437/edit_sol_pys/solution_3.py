

n = int(input())
s = input()

# first half and second half
a_count_first_half = s[:n//2].count('a')
b_count_first_half = s[:n//2].count('b')
a_count_second_half = s[n//2:].count('a')
b_count_second_half = s[n//2:].count('b')

# difference between first half and second half
difference = abs(a_count_first_half - b_count_first_half)
difference2 = abs(a_count_second_half - b_count_second_half)

# operations
operations = min(difference, difference2)

# output
print(operations)

# modified string output
if difference < difference2:
    print(s[:n//2] + s[n//2:])
else:
    print(s[n//2:] + s[:n//2])
