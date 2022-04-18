

n = int(input())
s = input()

# string
string = s[:n//2]
a_count_string = string.count('a')
b_count_string = string.count('b')

# last string
last_string = s[n//2:]
a_count_last_string = last_string.count('a')
b_count_last_string = last_string.count('b')

# difference
difference2 = abs(a_count_last_string - b_count_last_string)

# operations
operations = min(difference, difference2)

# output
print(operations)

# modified string
if difference < difference2:
    print(string + last_string)
else:
    print(last_string + string)
