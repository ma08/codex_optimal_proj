


def simplify(string):  # Simplify a string of lowercase letters.
    return len(set(string))  # Return the number of unique letters in the string.

def erase(string):  # Find minimum number of letters to erase to simplify a string.
    if len(string) < 3:  # If the length of the string is less than 3, it cannot be simplified.
        return 0  # Return 0 if the string cannot be simplified.
    if simplify(string) < 3:  # If the number of unique letters in the string is less than 3, it cannot be simplified.
        return 0  # Return 0 if the string cannot be simplified.
    for i in range(len(string)):  # Loop through the string.
        if simplify(string[:i] + string[i + 1:]) < 3:  # If the number of unique letters in the string without the ith letter is less than 3, erasing that letter will simplify the string.
            return 1  # Return 1 if erasing one letter will simplify the string.
    return 2  # Return 2 if erasing two letters will simplify the string.

print(erase(input()))  # Print the minimum number of letters to erase to simplify the string.
