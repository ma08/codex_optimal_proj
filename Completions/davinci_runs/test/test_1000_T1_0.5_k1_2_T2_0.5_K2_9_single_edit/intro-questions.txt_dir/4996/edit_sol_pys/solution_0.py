
# get input
message = input()
key = input()

# create the alphabet list
alphabet = []
for i in range(26):
    alphabet.append(chr(65+i))

# create the decrypted message
decrypted = ""
for i in range(len(message)):
    if i % 2 == 0:
        decrypted += alphabet[(alphabet.index(message[i]) - alphabet.index(key[i]) + 26) % 26]
    else:
        decrypted += alphabet[(alphabet.index(message[i]) + alphabet.index(key[i]) + 26) % 26]

# print the decrypted message
print(decrypted)
