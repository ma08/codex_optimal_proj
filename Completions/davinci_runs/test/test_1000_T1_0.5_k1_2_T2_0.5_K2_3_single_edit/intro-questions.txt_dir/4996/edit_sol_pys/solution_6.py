
def decrypt(c, k):
    decrypted = ""
    for i, j in zip(c, k):
            decrypted += chr((ord(i) - ord(j) + 26) % 26 + ord('A'))
    return decrypted

print(decrypt(input(), input()))
