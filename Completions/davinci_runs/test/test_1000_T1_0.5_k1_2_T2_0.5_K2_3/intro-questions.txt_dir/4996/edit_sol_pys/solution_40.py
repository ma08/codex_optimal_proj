

def encrypt(message, key):
    encrypted = ""
    for i in range(len(message) - 1):
        if i % 2 == 0:
            encrypted = encrypted + chr((ord(message[i]) + ord(key[i]) + 26) % 26 + ord('A'))
        else:
            encrypted = encrypted + chr((ord(message[i]) + ord(key[i]) - 26) % 26 + ord('A'))
    return encrypted

print(encrypt(input(), input()))
