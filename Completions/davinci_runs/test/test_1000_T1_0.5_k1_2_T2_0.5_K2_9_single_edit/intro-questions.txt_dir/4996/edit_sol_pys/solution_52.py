

# get input from the user
message = input("Enter the message: ")
key = input("Enter the key: ")

# create an alphabet list
alphabet = []
for i in range(26):
    alphabet.append(chr(65+i))

# create a decrypted message
decrypted = ""
for i in range(len(message)):
    if i % 2 == 0:
        decrypted += alphabet[(alphabet.index(message[i]) - alphabet.index(key[i]) + 26) % 26]
    else:
        decrypted += alphabet[(alphabet.index(message[i]) + alphabet.index(key[i]) + 26) % 26]

# print the decrypted message to the user
print("The decrypted message is: " + decrypted)
