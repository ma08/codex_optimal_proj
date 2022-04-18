

def vigenereCipherDecrypt(cipher, key, keyLength):
    i = 0
    decrypted = ""
    for char in cipher:
        if i % keyLength == 0:
            decrypted += chr(ord(char) - (ord(key[i % keyLength]) - ord('A')))
        else:
            decrypted += chr(ord(char) + (ord(key[i % keyLength]) - ord('A')))
        i += 1
    return decrypted

print(vigenereCipherDecrypt(input(), input(), len(input())))
