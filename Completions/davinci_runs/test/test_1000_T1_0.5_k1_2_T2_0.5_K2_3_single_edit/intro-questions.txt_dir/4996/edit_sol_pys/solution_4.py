

def encrypt(message, key):
    encrypted = ""
    for i in range(len(key)):
        encrypted += chr(((ord(message[i]) + ord(key[i])) % 26) + ord('A'))
    return encrypted

print(encrypt(input(), input()))
