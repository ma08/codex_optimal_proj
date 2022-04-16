

def kPeriodicString(string):
    if len(string) == 1:
        return 0
    for k in range(1, len(string)):
        if string[:k] == string[k:k*2]:
            return k*2
    return len(string)

print(kPeriodicString(input()))
