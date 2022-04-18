

def k_periodic_string(string):
    if len(string) == 1:
        return len(string)
    for k in range(1, int(len(string)/2) + 1):
        if string[:k] == string[k:k*2]:
            return k_periodic_string(string[k:])
    return len(string)

print(k_periodic_string(input()))
