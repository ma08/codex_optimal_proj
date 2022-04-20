

# SOLUTION
n = int(input()) # number of characters
s = input() # string

# Initialize the array with 1s
c = [1] * n

# Keep track of the last character that was colored
last = s[0]

# Keep track of the last color used
last_color = 1

# Loop through the characters in the string
for i in range(1, n):
    # If the current character is greater than the last character, then use the next color
    if s[i] > last:
        last_color += 1
    # Otherwise, use the same color
    else:
        last_color = 1
    # Update the color array
    c[i] = last_color
    # Update the last character
    last = s[i]

# Print the number of colors used
print(max(c))
# Print the color array
print(*c)
