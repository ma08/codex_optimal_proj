

def encrypt(message, key, keyLength):
    encrypted = ""
    for i in range(len(message) // keyLength):
        for j in range(keyLength):
            if j % 2 == 0:
                encrypted = encrypted + chr((ord(message[i + j]) + ord(key[j]) + 26) % 26 + ord('A'))
            else:
                encrypted = encrypted + chr((ord(message[i + j]) + ord(key[j]) - 26) % 26 + ord('A'))
    return encrypted

print(encrypt(input(), input(), int(input())))
