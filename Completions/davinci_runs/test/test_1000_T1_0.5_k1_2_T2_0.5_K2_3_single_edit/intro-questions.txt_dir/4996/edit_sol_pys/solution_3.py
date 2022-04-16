
def vigenereCipherDecrypt(cipher, key):
    i = 0
    decrypted = ""
    for char in cipher:
        decrypted += chr(ord(char) - (ord(key[i]) - ord('A')))
        i += 1
    return decrypted

print(vigenereCipherDecrypt(input(), input()))
