

def k_periodic(s):
    for k in range(1, len(s)):
        if s[:k] == s[k:]:
            return k
    return len(s) 

print(k_periodic(input()))
