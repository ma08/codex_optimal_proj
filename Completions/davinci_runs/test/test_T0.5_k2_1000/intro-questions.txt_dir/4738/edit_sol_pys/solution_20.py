

def k_periodic(s):  # периодичность
    k = 1
    while k < len(s):
        if s[:-k] == s[k:]:
            return k
        k += 1
    return len(s)

print(k_periodic(input()))
