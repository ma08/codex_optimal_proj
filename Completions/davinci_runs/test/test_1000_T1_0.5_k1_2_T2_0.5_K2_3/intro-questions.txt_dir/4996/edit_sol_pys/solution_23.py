

def decrypt(message, key):  # function to decrypt the message
    decrypted = ""  # decrypted message
    for i in range(len(message)):
        if i % 2 == 0:  # if the index of the character is even
            decrypted = decrypted + chr((ord(message[i]) - ord(key[i]) + 26) % 26 + ord('A'))
        else:  # if the index of the character is odd
            decrypted = decrypted + chr((ord(message[i]) - ord(key[i]) - 26) % 26 + ord('a'))
    return decrypted


print(decrypt(input(), input()))  # print the decrypted message
