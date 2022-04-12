

# get input
message = input()
key = input()

# create the alphabet list
alphabet = []
for i in range(26):
    alphabet.append(chr(65+i))

# create the encrypted message
encrypted = ""
for i in range(len(message)):
    if i % 2 == 0:
        encrypted += alphabet[(alphabet.index(message[i]) - alphabet.index(key[i % len(key)]) + 26) % 26]
    else:
        encrypted += alphabet[(alphabet.index(message[i]) + alphabet.index(key[i % len(key)]) + 26) % 26]

# print the encrypted message
print(encrypted)
