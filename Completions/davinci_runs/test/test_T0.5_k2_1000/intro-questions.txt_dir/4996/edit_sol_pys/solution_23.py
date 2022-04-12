

def vigenereCipherEncrypt(plain, key):
    i = 0
    encrypted = ""
    for char in plain:
        if i % 2 == 0:
            encrypted += chr(ord(char) + (ord(key[i]) - ord('A')))
        else:
            encrypted += chr(ord(char) - (ord(key[i]) - ord('A')))
        i += 1
    return encrypted

print(vigenereCipherEncrypt(input(), input()))
