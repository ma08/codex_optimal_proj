

def decrypt(c, k):
    decrypted = ''
    for i in range(len(c)):
        decrypted += chr((ord(c[i]) - ord(k[i])) % 26 + ord('A'))
    return decrypted

print(decrypt(input(), input()))
