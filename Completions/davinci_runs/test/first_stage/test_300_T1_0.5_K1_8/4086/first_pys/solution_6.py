

n = int(input())
a = list(map(int, input().split()))

# Find the last index of each element in the list
# The elements in the list should be unique
# So we can use a dictionary to store the last index of each element
# And then we can sort the dictionary by the values
# Finally, we use the keys of the dictionary to print the result

# Create a dictionary to store the last index of each element
last_index_of_element = {}

# Find the last index of each element in the list
# If the element is already in the dictionary
# Update the index
for i in range(n):
    if a[i] in last_index_of_element:
        last_index_of_element[a[i]] = i
    else:
        last_index_of_element[a[i]] = i

# Sort the dictionary by the values
sorted_dictionary = sorted(last_index_of_element.items(), key=lambda x: x[1])

# Print the result
print(len(sorted_dictionary))
for i in range(len(sorted_dictionary)):
    print(sorted_dictionary[i][0], end=" ")