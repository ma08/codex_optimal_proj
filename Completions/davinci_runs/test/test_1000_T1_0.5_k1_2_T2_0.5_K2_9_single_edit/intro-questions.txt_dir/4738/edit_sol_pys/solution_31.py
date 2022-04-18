

def k_periodic(s):
    for k in range(1, len(s)):
        if s[:k] == s[k:2 * k]:
            return k
    return len(s) - 1


print(k_periodic(input()))
