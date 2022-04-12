
def decrypt(cipher, key):
    plaintext = ""
    for i in range(len(cipher)):
        if i % 2 == 0:
            plaintext += chr((ord(cipher[i]) - ord(key[i]) + 26) % 26 + ord('A'))  # for even characters
        else:
            plaintext += chr((ord(cipher[i]) - ord(key[i]) - 26) % 26 + ord('A'))  # for odd characters
    return plaintext

print(decrypt(input(), input()))
