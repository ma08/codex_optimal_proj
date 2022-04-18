

def kPeriodicString(string):
    if len(string) == 1:
        return True
    for k in range(1, int(len(string)/2) + 1):
        if string[:k] == string[k:k*2]:
            return True
    return False

print(kPeriodicString(input()))
