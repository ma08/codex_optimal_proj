

def simplify(word):
    """Simplify a word of lowercase letters."""
    return len(set(word)) 

def erase(word):
    """Find minimum number of letters to erase to simplify a word."""
    if len(word) < 3:
        return 0 
    if simplify(word) < 3:
        return 0 
    for i in range(len(word)):
        if simplify(word[:i] + word[i + 1:]) < 3:
            return 1 
    return 2

print(erase(input())) 
