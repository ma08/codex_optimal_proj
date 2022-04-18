

def decrypt(message, key):
    decrypted = ""
    for i in range(len(message)):
        if i % 2 == 0:
            decrypted = decrypted + chr((ord(message[i]) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted = decrypted + chr((ord(message[i]) - ord(key[i]) - 26) % 26 + ord('a'))
    return decrypted

print(decrypt(input(), input()))
