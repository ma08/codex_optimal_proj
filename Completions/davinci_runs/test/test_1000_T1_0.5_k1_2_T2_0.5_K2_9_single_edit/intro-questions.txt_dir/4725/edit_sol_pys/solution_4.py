

def simplify(string):
    """Simplify a string of lowercase letters.
    
    Args:
        string (str): A string of lowercase letters.
    
    Returns:
        int: The number of unique letters in the string.
    """
    return len(set(string))

def erase(string):
    """Find minimum number of letters to erase to simplify a string."""
    if len(string) < 3:
        return 0
    if simplify(string) < 3:
        return 0
    for i in range(len(string)):
        if simplify(string[:i] + string[i + 1:]) < 3:
            return 1
    return 2

print(erase(input()))
