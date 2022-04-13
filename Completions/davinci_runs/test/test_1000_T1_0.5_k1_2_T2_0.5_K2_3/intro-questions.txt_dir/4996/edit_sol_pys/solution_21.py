
message = input().upper()
key = input().upper()

encrypted = []

for i in range(len(message)):
    shift = ord(key[i % len(key)]) - 65
    if i % 2 == 0:
        encrypted.append(chr((ord(message[i]) - shift + 26) % 26 + 65))
    else:
        encrypted.append(chr((ord(message[i]) + shift - 65) % 26 + 65))

print(''.join(encrypted))
