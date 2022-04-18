

def vigenereCipherEncrypt(cipher, key):
    i = 0
    encrypted = ''
    for char in cipher:
        if i % 2 == 0:
            encrypted += chr(ord(char) + (ord(key[i % len(key)]) - ord('A')))
        else:
            encrypted += chr(ord(char) - (ord(key[i % len(key)]) - ord('A')))
        i += 1
    return encrypted

print(vigenereCipherEncrypt(input(), input()))
