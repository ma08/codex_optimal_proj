
message = input("Enter the message: ")
key = input("Enter the key: ")

encrypted = []

for i in range(len(message)):
    shift = ord(key[i]) - 65
    if i % 2 == 0:
        encrypted.append(chr((ord(message[i]) - shift - 65) % 26 + 65))
    else:
        encrypted.append(chr((ord(message[i]) + shift - 65) % 26 + 65))

print(''.join(decrypted))
