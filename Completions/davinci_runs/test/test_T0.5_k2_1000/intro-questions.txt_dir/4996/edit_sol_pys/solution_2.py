

def encrypt(message, key, mode):
    encrypted = ""
    for i in range(len(message)):
        if mode == "e":
            encrypted = encrypted + chr((ord(message[i]) - ord(key[i]) + 26) % 26 + ord('A'))
        else:
            encrypted = encrypted + chr((ord(message[i]) - ord(key[i]) - 26) % 26 + ord('A'))
    return encrypted

print(encrypt(input(), input(), input()))
