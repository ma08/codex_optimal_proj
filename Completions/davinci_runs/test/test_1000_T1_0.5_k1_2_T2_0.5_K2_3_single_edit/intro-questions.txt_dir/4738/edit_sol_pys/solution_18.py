

def kPeriodicString(string):
    for k in range(1, int(len(string)/2) + 1):
        if string[:k] == string[k:k*2]:
            return k
    return len(string)

print(kPeriodicString(input()))
