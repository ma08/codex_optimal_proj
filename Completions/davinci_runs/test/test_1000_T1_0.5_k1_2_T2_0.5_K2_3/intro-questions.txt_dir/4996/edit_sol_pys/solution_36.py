

# get input from user
message = input("Enter a message to encrypt: ")
key = input("Enter a key: ")

# create the alphabet list
alphabet = []
for i in range(26):
    alphabet.append(chr(65+i))

# create the encrypted message by subtracting the index of the key character and the index of the message character (if i % 2 == 0) or by adding the index of the key character and the index of the message character (if i % 2 == 1)
encrypted = ""
for i in range(len(message)):
    if i % 2 == 0:
        encrypted += alphabet[(alphabet.index(message[i]) - alphabet.index(key[i]) + 26) % 26]
    else:
        encrypted += alphabet[(alphabet.index(message[i]) + alphabet.index(key[i]) + 26) % 26]

# print the encrypted message to the user
print(encrypted)
