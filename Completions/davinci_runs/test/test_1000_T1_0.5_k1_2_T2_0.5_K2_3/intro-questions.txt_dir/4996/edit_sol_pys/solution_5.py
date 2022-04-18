

def decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        if i % 2 == 0:
            plaintext += chr((ord(ciphertext[i]) - ord(key[i]) + 26) % 26 + 65)
        else:
            plaintext += chr((ord(ciphertext[i]) - ord(key[i]) - 26) % 26 + 65)
    return plaintext

print(decrypt(input(), input()))
