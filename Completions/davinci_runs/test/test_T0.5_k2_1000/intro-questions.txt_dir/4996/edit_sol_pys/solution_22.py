
def decrypt(cipher, key):
    plaintext = ""
    for i in range(len(cipher)):
        if i % 2 == 0:
            plaintext += chr((ord(cipher[i]) - ord(key[i]) + 26) % 26 + ord('A'))
        else:
            plaintext += chr((ord(cipher[i]) - ord(key[i]) - 26) % 26 + ord('A'))
    return plaintext

print(decrypt(input(), input())) 
