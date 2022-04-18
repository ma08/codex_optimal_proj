

def kPeriodicString(s): 
    if len(s) == 1:
        return 1
    for i in range(1, int(len(s)/2) + 1):
        if s[:i] == s[i:i*2]:
            return i
    return len(s)

print(kPeriodicString(input()))
