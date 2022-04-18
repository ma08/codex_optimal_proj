

def k_periodic(s, k):
    for i in range(1, len(s) // 2 + 1):
        if s[:i] == s[i:i*2]:
            return i
    return -1

print(k_periodic(input(), int(input())))
