

def k_periodic(s, k):
    while k < len(s) / 2:
        if s[:k] == s[k:k*2]:
            return k
        k += 1
    return -1

print(k_periodic(input(), int(input())))
