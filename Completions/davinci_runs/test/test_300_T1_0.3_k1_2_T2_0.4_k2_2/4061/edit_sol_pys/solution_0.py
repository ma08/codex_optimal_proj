

s = input()
t = input()

# s = "bbaba"
# t = "bb"

# s = "baaba"
# t = "ab"

# s = "abcde"
# t = "abcde"

# s = "asdfasdf"
# t = "fasd"

def max_substring(s, t):
    # Initialize the max_length to be the length of the first character
    max_length = len(t)
    # Initialize the current_length to be the length of the first character
    current_length = len(t)
    # Initialize the index to be 0
    index = 0
    # Initialize the current_index to be 0
    current_index = 0
    # Loop through the length of the string
    for i in range(len(s)):
        # If the current character is equal to the current character in t
        if s[i] == t[current_index]:
            # Increment the current_index
            current_index += 1
            # If the current_index is equal to the length of t
            if current_index == len(t):
                # Reset the current_index
                current_index = 0
                # Set the index to be the current index
                index = current_index
                # Set the current_length to be the current index
                current_length = current_index
            # If the current index is greater than the length of t
            elif current_index > len(t):
                # Set the current_length to be the current index minus the index
                current_length = current_index - index
        # If the current character is not equal to the current character in t
        else:
            # If the current index is greater than the length of t
            if current_index > len(t):
                # Set the current_length to be the current index minus the index
                current_length = current_index - index
            # If the current index is less than the length of t
            else:
                # Set the current_length to be the current index
                current_length = current_index
        # If the current length is greater than the max length
        if current_length > max_length:
            # Set the max length to be the current length
            max_length = current_length
    # Return the max length
    return max_length

print(max_substring(s, t))
