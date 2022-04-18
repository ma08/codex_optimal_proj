

def decrypt(c, k):
    decrypted = ""
    for i in range(len(c)):
        if i % 2 == 0:
            decrypted += chr((ord(c[i]) - ord(k[i]) + 26) % 26 + ord("A"))
        else:
            decrypted += chr((ord(c[i]) - ord(k[i]) - 26) % 26 + ord("A"))
    return decrypted

print(decrypt(input(), input()))
