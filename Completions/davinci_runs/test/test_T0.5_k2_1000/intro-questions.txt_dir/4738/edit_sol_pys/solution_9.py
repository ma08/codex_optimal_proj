

def k_periodic_string(s, k):
    if s[:-k] == s[k:]:
        return True
    return False

print(k_periodic_string(input()))
