

def encrypt(message, key):
    encrypted = ""
    for i in range(len(message)):
        if i % 2 == 0:
            encrypted = encrypted + chr((ord(message[i]) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            encrypted = encrypted + chr((ord(message[i]) - ord(key[i]) - 26) % 26 + ord('a'))
    return encrypted

print(encrypt(input(), input()))
