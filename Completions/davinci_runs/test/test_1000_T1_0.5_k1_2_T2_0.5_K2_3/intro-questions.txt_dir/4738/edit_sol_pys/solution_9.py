

def kPeriodicString(s): 
    for k in range(1, int(len(s) / 2) + 1):
        if s[:k] == s[k:k*2]:
            return k
    return len(s)

print(kPeriodicString(input()))
