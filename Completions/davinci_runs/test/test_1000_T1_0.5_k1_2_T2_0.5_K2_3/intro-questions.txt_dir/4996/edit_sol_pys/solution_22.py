
def shift(c, key, i): # i is the index of the char in the key
    return chr((ord(c) - ord('A') + (1 if i % 2 == 0 else -1) * (ord(key[i]) - ord('A'))) % 26 + ord('A'))

c = input()
k = input()
print("".join(shift(c[i], k, i) for i in range(len(c))))
