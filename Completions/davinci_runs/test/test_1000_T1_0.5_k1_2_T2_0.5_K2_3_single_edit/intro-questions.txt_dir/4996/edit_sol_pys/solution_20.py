

def vigenere_cipher_decrypt(cipher, key):
    i = 0
    decrypted = ""
    for char in cipher:
        if i % 2 == 0:
            decrypted += chr(ord(char) + (ord(key[i]) - ord('A')))
        else:
            decrypted += chr(ord(char) - (ord(key[i]) - ord('A')))
        i += 1
    return decrypted

print(vigenere_cipher_decrypt(input(), input()))
