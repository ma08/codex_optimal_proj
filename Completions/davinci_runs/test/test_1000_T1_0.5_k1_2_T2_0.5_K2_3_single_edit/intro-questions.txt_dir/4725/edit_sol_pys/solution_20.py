

def simplify(string):
    """Simplify a string of lowercase letters."""
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

if __name__ == '__main__':
    print(erase(input()))
