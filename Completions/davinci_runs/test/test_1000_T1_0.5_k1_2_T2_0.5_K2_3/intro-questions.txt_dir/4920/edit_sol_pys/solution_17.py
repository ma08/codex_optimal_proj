

# My solution

s = input()

# Create a dictionary of the number of occurrences of each letter in s
occurrences = {}
for char in s:
    if char in occurrences:
        occurrences[char] += 1
    else:
        occurrences[char] = 1

# Create a list of the number of occurrences of each letter in s
occurrences_list = []
for key, value in occurrences.items():
    occurrences_list.append(value)

# Create a list of the number of occurrences of each letter in s that are greater than 1
occurrences_list_gt1 = []
for num in occurrences_list:
    if num > 1:
        occurrences_list_gt1.append(num)

# Create a list of the number of occurrences of each letter in s that are greater than 1 and subtract 1 from each number
occurrences_list_gt1_sub1 = []
for num in occurrences_list_gt1:
    occurrences_list_gt1_sub1.append(num - 1)

# Create a list of the number of occurrences of each letter in s that are greater than 1 and subtract 1 from each number and multiply all the numbers in the list together
# and multiply all the numbers in the list together
occurrences_list_gt1_sub1_mult = 1
for num in occurrences_list_gt1_sub1:
    occurrences_list_gt1_sub1_mult *= num

# Create a list of the number of occurrences of each letter in s that are greater than 1 and subtract 1 from each number and multiply all the numbers in the list together
# and multiply that number by the number of occurrences of each letter in s that are equal to 1
occurrences_list_gt1_sub1_mult_mult1 = occurrences_list_gt1_sub1_mult * len(occurrences)

# Print the number of occurrences of each letter in s that are greater than 1 and subtract 1 from each number
# and multiply all the numbers in the list together and multiply that number by the number of occurrences of each letter in s that are equal to 1
print(occurrences_list_gt1_sub1_mult_mult1)
