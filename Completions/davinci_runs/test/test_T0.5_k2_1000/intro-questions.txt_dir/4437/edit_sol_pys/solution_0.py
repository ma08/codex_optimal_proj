

n = int(input())
s = input()

# first half of string and second half of string
first_half_of_string = s[:n//2] 
second_half_of_string = s[n//2:]

# a count and b count
a_count_first_half_of_string = first_half_of_string.count('a') 
b_count_first_half_of_string = first_half_of_string.count('b') 
a_count_second_half_of_string = second_half_of_string.count('a') 
b_count_second_half_of_string = second_half_of_string.count('b') 

# difference and difference2
difference = abs(a_count_first_half_of_string - b_count_first_half_of_string)
difference2 = abs(a_count_second_half_of_string - b_count_second_half_of_string)

# operations 
operations = min(difference, difference2)

# output
print(operations)

# modified string
if difference < difference2:
    print(first_half_of_string + second_half_of_string)
else:
    print(second_half_of_string + first_half_of_string)
