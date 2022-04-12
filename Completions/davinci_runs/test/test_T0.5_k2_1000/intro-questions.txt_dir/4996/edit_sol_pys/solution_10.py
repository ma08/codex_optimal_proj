

def vigenereCipherEncrypt(plain, key, encrypt):
    i = 0
    encrypted = ""
    for char in plain:
        if encrypt:
            encrypted += chr(ord(char) + (ord(key[i % len(key)]) - ord('A')))
        else:
            encrypted += chr(ord(char) - (ord(key[i % len(key)]) - ord('A')))
        i += 1
    return encrypted

print(vigenereCipherEncrypt(input(), input(), True))
