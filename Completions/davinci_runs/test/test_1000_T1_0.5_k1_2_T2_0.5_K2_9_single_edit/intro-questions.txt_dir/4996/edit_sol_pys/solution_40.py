

def decrypt(message, key, offset):
    decrypted = ""
    for i in range(len(message)):
        if i % 2 == 0:
            decrypted = decrypted + chr((ord(message[i]) - ord(key[i]) + offset) % 26 + ord('A'))
        else:
            decrypted = decrypted + chr((ord(message[i]) - ord(key[i]) - offset) % 26 + ord('A'))
    return decrypted

print(decrypt(input(), input()))
