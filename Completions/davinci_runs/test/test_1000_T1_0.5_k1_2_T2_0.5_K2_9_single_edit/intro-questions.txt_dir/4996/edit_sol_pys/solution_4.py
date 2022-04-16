

def vigenereCipherDecrypt(cipher, key):
    i = 0 
    decrypted = ""
    for char in cipher:
        if char.isalpha():
            if i % 2 == 0:
                decrypted += chr(ord(char) + (ord(key[i]) - ord('A')))
            else:
                decrypted += chr(ord(char) - (ord(key[i]) - ord('A')))
            i += 1
        else:
            decrypted += char
    return decrypted

print(vigenereCipherDecrypt(input(), input().upper()))
