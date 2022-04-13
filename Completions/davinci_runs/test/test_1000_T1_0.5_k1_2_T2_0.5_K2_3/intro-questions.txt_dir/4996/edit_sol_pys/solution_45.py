

def vigenereCipherEncrypt(cipher, key, encrypted):
    i = 0
    for char in cipher:
        if i % 2 == 0:
            encrypted += chr(ord(char) + (ord(key[i]) - ord('A')))
        else:
            encrypted += chr(ord(char) - (ord(key[i]) - ord('A')))
        i += 1
    return encrypted

print(vigenereCipherEncrypt(input(), input(), ""))
