
message = input()
key = input()

decrypted = []

for i in range(len(message)):
    shift = ord(key[i % len(key)]) - 65
    if i % 2 == 0:
        decrypted.append(chr((ord(message[i]) - shift - 65) % 26 + 65))
    else:
        decrypted.append(chr((ord(message[i]) + shift - 65) % 26 + 65))

print(''.join(decrypted))
