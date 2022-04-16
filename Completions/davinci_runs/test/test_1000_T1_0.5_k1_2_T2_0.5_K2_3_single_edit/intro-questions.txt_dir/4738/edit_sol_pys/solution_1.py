

def kPeriodicString(s):
    for k in range(1, int(len(s) / 2) + 1):
        if len(s) % k == 0:
            if s[:k] * (len(s) // k) == s:
                return k
    return len(s) 

print(kPeriodicString(input()))
