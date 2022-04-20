

n = int(input())
s = input()

# Initialize the number of cubes that can be removed
num_cubes_removed = 0

# Initialize the number of consecutive red cubes
num_consec_red = 0

# Initialize the number of consecutive blue cubes
num_consec_blue = 0

# Iterate through each cube
for i in range(n):
    # If the cube is red
    if s[i] == '0':
        # Increment the number of consecutive red cubes
        num_consec_red += 1
        # If there are two or more consecutive red cubes
        if num_consec_red >= 2:
            # Increment the number of cubes that can be removed
            num_cubes_removed += 1
            # Reset the number of consecutive red cubes
            num_consec_red = 0
        # Reset the number of consecutive blue cubes
        num_consec_blue = 0
    # If the cube is blue
    else:
        # Increment the number of consecutive blue cubes
        num_consec_blue += 1
        # If there are two or more consecutive blue cubes
        if num_consec_blue >= 2:
            # Increment the number of cubes that can be removed
            num_cubes_removed += 1
            # Reset the number of consecutive blue cubes
            num_consec_blue = 0
        # Reset the number of consecutive red cubes
        num_consec_red = 0

# Print the number of cubes that can be removed
print(num_cubes_removed)
