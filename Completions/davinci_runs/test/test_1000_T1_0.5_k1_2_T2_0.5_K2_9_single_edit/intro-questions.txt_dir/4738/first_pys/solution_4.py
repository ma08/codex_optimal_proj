

def kPeriodicString(s):
    if len(s) == 1:
        return 1
    for k in range(1, int(len(s)/2) + 1):
        if s[:k] == s[k:k*2]:
            return k
    return len(s)

print(kPeriodicString(input()))