
def decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)): # iterate through each character of the ciphertext
        if i % 2 == 0: # even characters
            plaintext += chr((ord(ciphertext[i]) - ord(key[i]) + 26) % 26 + ord('A')) # add a character to the plaintext
        else: # odd characters
            plaintext += chr((ord(ciphertext[i]) - ord(key[i]) - 26) % 26 + ord('A')) # add a character to the plaintext
    return plaintext

print(decrypt(input(), input()))
