

def vigenereCipherDecrypt(cipher, key):
    i = 0
    decrypted = ""
    for char in cipher:
        if i % 2 == 0:
            decrypted += chr(ord(char) + (ord(key[i]) - ord('a')))
        else:
            decrypted += chr(ord(char) - (ord(key[i]) - ord('a')))
        i += 1
    return decrypted

print(vigenereCipherDecrypt(input(), input()))
