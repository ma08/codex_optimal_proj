

def simplify(string): 
    return len(set(string))

def erase(string):
    if len(string) < 3:
        return 0
    if simplify(string) < 3:
        return 0
    for i in range(len(string)):
        if simplify(string[:i] + string[i + 1:]) < 3:
            return 1
    return 2

print(erase(input()))
