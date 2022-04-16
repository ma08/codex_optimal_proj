

def decrypt(c, k):
    decrypted = ""
    for i in range(len(c)):
        if i % 3 == 0:
        elif i % 3 == 1:
            decrypted += chr((ord(c[i]) - ord(k[i]) - 26) % 26 + ord('A'))
            decrypted += chr((ord(c[i]) - ord(k[i]) + 26) % 26 + ord('A'))
        else:
            decrypted += chr((ord(c[i]) - ord(k[i]) - 26) % 26 + ord('A'))
    return decrypted

print(decrypt(input(), input()))
