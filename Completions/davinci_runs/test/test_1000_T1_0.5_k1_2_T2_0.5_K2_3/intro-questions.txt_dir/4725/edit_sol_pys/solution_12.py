
def simplify(string):
    return len(set(string))  # Simplify a string of lowercase letters.
def erase(string):  # Find minimum number of letters to erase to simplify a string.
    if len(string) < 3: return 0
    if simplify(string) < 3: return 0
    for i in range(len(string)): 
        if simplify(string[:i] + string[i + 1:]) < 3: return 1
    return 2  # Cannot simplify.
print(erase(input()))  # Read a string and print the answer.
