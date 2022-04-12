

def k_periodic_string(s):
    for k in range(1, len(s)):
        if s[:k] == s[k:]:
            return len(s)//k
    return len(s) 

print(k_periodic_string(input()))
