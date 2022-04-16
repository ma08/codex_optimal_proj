

# Read input as string
input_string = str(input())

# Convert string to list
input_list = input_string.split()

# Convert list items to int
input_list = [int(i) for i in input_list]

# Read first item of the list
a = input_list[0]

# Read second item of the list
b = input_list[1]

# Print the sum of a and b
print(a + b)
